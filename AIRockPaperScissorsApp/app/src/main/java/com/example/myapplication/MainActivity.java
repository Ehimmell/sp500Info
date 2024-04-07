/* Code that prompts the user to take a picture, extracts the RGB values from each pixel in the image, classifies it via tfLite model, and displays what the user should play
in order to counter what the model classified the given image as. 

While I, Ethan Himmell, wrote a majority of this code, the code used to feed and extract RGB values was taken from an individual known as ishaanjav on GitHub.
This individual created a very similar project as I did 2 years before I started this, and when I was curious on how to integrate my TFLite model to Android Studio,
I came across his work. While it's licensed under an MIT License, which allows virtually unrestricted use, I still feel grateful that I was able to utilize a part of 
ishaanjav's code to save time, and want to give credit where it is due.

Created by Ethan Himmell on April 7, 2024. */

package com.example.myapplication;


import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.media.ThumbnailUtils;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;


import com.example.myapplication.ml.NewModel;

import org.tensorflow.lite.DataType;
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;


public class MainActivity extends AppCompatActivity {
    //Initialize Screen Elements from main activity
    Button camera;
    ImageView imageView;

    ImageView counterView;
    TextView result;

    TextView counter;
    int imageSize = 32;

    int requestCode;

    //Set on create behavior, or what the app should do upon being opened
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Relate the various components I created earlier to their actual layout counterparts
        camera = findViewById(R.id.button);

        result = findViewById(R.id.result);

        counter = findViewById(R.id.counterresult);

        imageView = findViewById(R.id.imageView);

        counterView = findViewById(R.id.imageView2);

        //Set onClickListener, or what the button should do upon click
        camera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                //Checks if cmaera permissions are given, if so prompt the user to take a picture. If not, request them.
                if (checkSelfPermission(Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
                    Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                    requestCode = 3;
                    activityResultLauncher.launch(cameraIntent);
                } else {
                    requestPermissions(new String[]{Manifest.permission.CAMERA}, 100);
                }
            }
        });
    }

    public void classifyImage(Bitmap image){
        try {

            //Initialize Model
            NewModel model = NewModel.newInstance(getApplicationContext());


            //ishaanjav's code
            // Creates inputs for reference with correct dimensions
            TensorBuffer inputFeature0 = TensorBuffer.createFixedSize(new int[]{1, 32, 32, 3}, DataType.FLOAT32);
            ByteBuffer byteBuffer = ByteBuffer.allocateDirect(4 * imageSize * imageSize * 3);
            byteBuffer.order(ByteOrder.nativeOrder());
            
            int[] intValues = new int[imageSize * imageSize];
            image.getPixels(intValues, 0, image.getWidth(), 0, 0, image.getWidth(), image.getHeight());
            int pixel = 0;
            //iterate over each pixel and extract R, G, and B values. Add those values individually to the byte buffer.
            for(int i = 0; i < imageSize; i ++){
                for(int j = 0; j < imageSize; j++){
                    int val = intValues[pixel++]; // RGB
                    byteBuffer.putFloat(((val >> 16) & 0xFF) * (1.f / 1));
                    byteBuffer.putFloat(((val >> 8) & 0xFF) * (1.f / 1));
                    byteBuffer.putFloat((val & 0xFF) * (1.f / 1));
                }
            }

            inputFeature0.loadBuffer(byteBuffer);


            //Back to my code
            // Runs model and gets the model's image prediction
            NewModel.Outputs outputs = model.process(inputFeature0);
            TensorBuffer outputFeature0 = outputs.getOutputFeature0AsTensorBuffer();

            float[] confidences = outputFeature0.getFloatArray();
            // find which class the AI is most confident the image falls into
            int maxPos = 0;
            float maxConfidence = 0;
            for (int i = 0; i < confidences.length; i++) {

                //If the current confidence is greater than the highest, new highest is current confidence
                if (confidences[i] > maxConfidence) {
                    maxConfidence = confidences[i];
                    maxPos = i;
                }
            }

            //Define Different classes for images to fall under
            String[] classes = {"Paper", "Rock", "Scissors"};

            //Run a switch on the AI's prediction, and set the "counter move" accordingly
            switch (classes[maxPos]) {
                case "Paper":
                    counter.setText(classes[2]);
                    counterView.setImageResource(R.drawable.scissors);
                    break;
                case "Rock":
                    counter.setText(classes[0]);
                    counterView.setImageResource(R.drawable.paper);
                    break;
                case "Scissors":
                    counter.setText(classes[1]);
                    counterView.setImageResource(R.drawable.rock);
                    break;
            }
            result.setText(classes[maxPos]);

            // Releases model resources if no longer used.
            model.close();
        } catch (IOException e) {
        }
    }

    //Method to tell the onclicklistener to do once it has received an image
    ActivityResultLauncher<Intent> activityResultLauncher = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            new ActivityResultCallback<ActivityResult>() {

                    @Override
                    //Define received image behavior
                    public void onActivityResult(ActivityResult result) {
                        int resultCode = result.getResultCode();
                        Intent data = result.getData();
                        if(resultCode == RESULT_OK){

                                //gets the image and gives it to the classifyimage method
                                Bitmap image = (Bitmap) data.getExtras().get("data");
                                int dimension = Math.min(image.getWidth(), image.getHeight());
                                image = ThumbnailUtils.extractThumbnail(image, dimension, dimension);
                                imageView.setImageBitmap(image);

                                image = Bitmap.createScaledBitmap(image, imageSize, imageSize, false);
                                classifyImage(image);
                        }
                    }
            });
}
