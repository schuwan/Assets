drop table if exists image_locations cascade;
drop table if exists users cascade;
drop table if exists posts cascade;
drop table if exists post_comments cascade;
drop table if exists user_likes cascade;
drop table if exists post_images cascade;
drop table if exists branch_locations cascade;
drop table if exists profile_pictures cascade;
drop table if exists genders cascade;


create table if not exists image_locations(
--  col_name              col_datatype     other_constraints
    id                    serial,
    url                   varchar(200)     unique not null,
    
    primary key(id)
    
    );
   
create table if not exists genders(
--  col_name              col_datatype     other_constraints
    id                    serial,
    gender                varchar(16)      unique not null,
   
   primary key(id)

	);

create table if not exists profile_pictures(
--  col_name              col_datatype     other_constraints
   id                     serial,
   image_location         int              not null,
   image_name             varchar(50)      unique not null,
   
   primary key(id),
    
    foreign key (image_location) references image_locations(id) 
    	on delete no action 
    	on update cascade
   );

create table if not exists branch_locations(
--  col_name              col_datatype     other_constraints
   id                     serial,
   branch_name            varchar(50)      unique not null,
   city                   varchar(50)      not null,
   state                  varchar(50)      not null,
   country                varchar(50)      not null,
   
   primary key(id)
   );

create table if not exists users(
--  col_name              col_datatype     other_constraints
    id                    serial,
    username              varchar(50)      unique not null, 
    email                 varchar(150)     unique not null,
    first_name            varchar(50)      not null, 
    last_name             varchar(50)      not null,
    passwrd               varchar(24)      not null,
    date_of_birth         timestamp        not null,
    gender                int              not null, 
    branch                int              not null, 
    profile_picture       int, 
    
    primary key(id),
    
    foreign key (gender) references genders(id) 
    	on delete no action 
    	on update cascade,
    foreign key (branch) references branch_locations(id) 
        on delete no action 
        on update cascade,
    foreign key (profile_picture) references profile_pictures(id)
        on delete set null
        on update cascade      
 	);
 
 create table if not exists posts(
--  col_name              col_datatype     other_constraints
    id                    serial,
    poster_id             int,
    title                 varchar(100),
    body                  text             not null, 
    created               timestamp        not null, 
    last_edited           timestamp, 
    
    primary key(id),
    
    foreign key (poster_id) references users(id) 
    	on delete set null 
    	on update cascade
    );
    
  
  create table if not exists post_images(
--  col_name              col_datatype     other_constraints
    id                    serial,
    post_id               int,
    image_location        int              not null,
    image_name            varchar(100)     unique not null,
    image_title           varchar(50), 
    
    primary key(id),
    
    foreign key (post_id) references posts(id)
    	on delete cascade
    	on update cascade,
		
	foreign key (image_location) references image_locations(id) 
    	on delete no action 
    	on update cascade
    );
   
   
  create table if not exists user_likes(
--  col_name              col_datatype     other_constraints
	post_id               int, 
	user_id               int,
	
	primary key(post_id, user_id),
	
	foreign key (post_id) references posts(id)
    	on delete set null
    	on update cascade,
    	
    foreign key (user_id) references users(id)
    	on delete set null
    	on update cascade
   );
    
  create table if not exists post_comments(
--  col_name              col_datatype     other_constraints
    id                    serial,
    post_id               int,
    commenter_id          int, 
    message               text             not null, 
    created               timestamp        not null, 
    
    primary key(id),
    
    foreign key (post_id) references posts(id)
    	on delete set null
    	on update cascade,
    
     foreign key (commenter_id) references users(id)
    	on delete set null
    	on update cascade
   );
   
  
  insert into genders(gender) values ('Male'),('Female'),('Other');
  insert into branch_locations(branch_name, city, state, country) values
  	('DC Office', 'Reston', 'VA', 'USA'),
  	('New York Office', 'New York', 'NY', 'USA'),
  	('Dallas Office', 'Dallas', 'TX', 'USA'),
  	('Olando Office', 'Orlando', 'FL', 'USA'),
  	('West Virgina University', 'Morgantown', 'WV', 'USA')
  ;