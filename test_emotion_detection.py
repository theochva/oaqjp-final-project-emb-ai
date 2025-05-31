"""
Unit tests for package EmotionDetection
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Each entry of the test data is an str array with 2 elements:
        # - elem 0: the "text to analyze"
        # - elem 1: the "expected" dominant emotion to get when calling the function
        test_data = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]

        # Loop through the test data annd run the function and check
        for text_to_analyze, exp_dominant_emotion in test_data:
            result = emotion_detector(text_to_analyze)
            self.assertEqual(exp_dominant_emotion, result['dominant_emotion'])

# Run the unit test
unittest.main()