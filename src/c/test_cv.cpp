#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;

/** Function Headers */
void detectAndDisplay(Mat frame);

/** Globals */
String face_cascade_name = "haarcascade_frontalface_default.xml";
CascadeClassifier face_cascade;
String window_name = "Face Capture";
RNG rng(12345);

/** @function main */
int main(int argc, const char** argv)
{
  CvCapture* capture;
  Mat frame;

  // Load the cascades.
  if (!face_cascade.load(face_cascade_name)) { printf("Error loading."); return -1; };

  // Read the video stream.
  capture = cvCaptureFromCAM(-1);

  if (capture)
  {
    while (true)
    {
      frame = cvQueryFrame(capture);

      // Apply the classifier to the frame.
      if (!frame.empty())
      {
        detectAndDisplay(frame);
      } else
      {
        printf("No capture from frame. Break.");
        break;
      }

      int c = waitKey(10);
      if ((char) c == 'c')
      {
        break;
      }
    }
  }
  return 0;
}

/** @function detectAndDisplay */
void detectAndDisplay(Mat frame)
{
  std::vector<Rect> faces;
  Mat frame_gray;

  cvtColor(frame, frame_gray, CV_BGR2GRAY);
  equalizeHist(frame_gray, frame_gray);

  // Detect Faces
  face_cascade.detectMultiScale(frame_gray, faces, 1.1, 2, CV_HAAR_SCALE_IMAGE, Size(30, 30));

  for (size_t i = 0 ; i < faces.size() ; i++)
  {
    Point center(faces[i].x + faces[i].width * 0.5, faces[i].y + faces[i].height * 0.5);
    ellipse(frame, center, Size(faces[i].width * 0.5, faces[i].height * 0.5), 0, 0, 360, Scalar(255, 0, 255), 4, 8, 0);

    Mat faceROI = frame_gray(faces[i]);
  }
  imshow(window_name, frame);
}
