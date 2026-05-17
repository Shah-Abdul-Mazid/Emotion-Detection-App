import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test Joy
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')
        
        # Test Anger
        self.assertEqual(emotion_detector("I am really mad at you")['dominant_emotion'], 'anger')
        
        # Test Sadness
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness')
        
        # Test Fear
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear')
        
        # Test Disgust
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')

if __name__ == '__main__':
    unittest.main()