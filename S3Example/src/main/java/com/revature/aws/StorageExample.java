package com.revature.aws;

import com.amazonaws.auth.EnvironmentVariableCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

import java.io.ByteArrayInputStream;
import java.io.File;

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

        /* Put a file into the bucket.
        * The first variable is the bucket name, this will always be reverse-social-media for us
        * The second name is key/file name, this must be unique within a folder of the bucket
        * The third argument can be either a file object, or an input stream
         */
        amazonS3.putObject("reverse-social-media", "test.png", new File("test.png"));

        /* Get the url of a file.
        * The first argument is the bucket name
        * The second argument is the key/file name
         */
        System.out.println(amazonS3.getUrl("reverse-social-media", "test.png"));

    }

}
