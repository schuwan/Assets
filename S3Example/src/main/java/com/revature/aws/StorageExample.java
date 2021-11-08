package com.revature.aws;

import com.amazonaws.auth.EnvironmentVariableCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.ObjectMetadata;
import org.joda.time.DateTime;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.util.Base64;
import java.util.Date;

public class StorageExample {

    public static void main(String... args) {
        new StorageExample().start();
    }

    public void start() {
        /*
        * Connects to the S3 server, I'm using the environment credentials provider.
        * The environment credentials provider expects the AWS_ACCESS_KEY and AWS_SECRET_KEY environment variables to be set.
        * Contact Ryan to get the values for those
        */
        AmazonS3 amazonS3 = AmazonS3ClientBuilder.standard().withCredentials(new EnvironmentVariableCredentialsProvider())
                // Sets the region to us-east-1 which is where the s3 is located
                .withRegion(Regions.US_EAST_1).build();

        /*
         * Take a byte string and convert it to a ByteArrayInputStream
         */
        String byteString = "iVBORw0KGgoAAAANSUhEUgAAAHgAAABACAIAAABeLyRFAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIOSURBVHhe7ZXhccMgDEYzVwbyPJnGy2SYVFJwkBDGvpp+be++9ycIgZBec+ntRSBQNAiKBkHRICgaBEWDoGgQFA2CokFQNAiKBkHRICgaBEWDoGgQFA2CokFQNAiKBkHRICgaBEWDoGgQFA0CIXpdbrdlzevfZdzJ9D7PiZZn749nCT48H/fedoKiBYruQ9HT+M+idWPDdTkUrRsfuqPpCfeMPVIPxiZ2q5Vj77ydbztxzct2m73MPNFBQAh802EADdw4dqnzThzaLtVTEpZgWM0in45V412LwuHrnBa9wzaJDhIcuTn8SG6drhQdeb6mwLLUv7vesNRBtVx52Ek+fpVJ3+h+q2Wn8VTW+YrQ3fTv22qVU7WIrY6q5fy4E9/zFCaK7vBu1Tc9Hu/wJVnop8ZWRY6fq5bz405qdhI/9o12+KbH4+3W0X25Jh/vbFnUvo6q5fy4E9/zFGb9M+wOWvBNu3Xnyn4VzSzrumxZ60h+Qj6nD6rltOtElzn5N0XnbtelIzesLXDjNGFEHhPCXd0IDw6qDUVbtqYtGrTyLeaJFmy2jTjyFvm1sg1ldN6oWHF3tY2V/Wqp17YTf1W22z4vc040uQxFg6BoEBQNgqJBUDQIigZB0SAoGgRFg6BoEBQNgqJBUDQIigZB0SAoGgRFg6BoEBQNgqJBUDQIigZB0SAoGgRFg6BoCK/XF4C0vgY0hZPwAAAAAElFTkSuQmCC";
        byte[] bytes = Base64.getDecoder().decode(byteString);

        ByteArrayInputStream in = new ByteArrayInputStream(bytes);

        /*
         * Create and set metadata
         */
        ObjectMetadata meta = new ObjectMetadata();
        meta.setContentEncoding("base64");
        meta.setContentType("image/png");
        meta.setContentLength(bytes.length);
        meta.setLastModified(DateTime.now().toDate());

        /* Put a file into the bucket.
         * The first variable is the bucket name, this will always be reverse-social-media for us
         * The second name is key/file name, this must be unique within a folder of the bucket
         * The third argument is the input stream
         * The fourth is the metadata
         */

        amazonS3.putObject("reverse-social-media", "test.png", in, meta);

        /* Get the url of a file.
        * The first argument is the bucket name
        * The second argument is the key/file name
         */
        System.out.println(amazonS3.getUrl("reverse-social-media", "test.png").toString());

    }

}
