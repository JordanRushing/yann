"""
test_activations.py - Unit tests for YANN core activation functions
defined in yann/core/activations.py
"""

import unittest
import numpy as np
import theano
import theano.tensor as T
import yann.core.activations as A


class TestActivations(unittest.TestCase):
    """
    expected_array values are precomputed using a Python interpreter,
    numpy_input, and the corresponding activation function.

    .shape is used to check the dimensionality of the result while
    .allclose checks the element-wise equality of the result
    """

    def setUp(self):
        """
        numpy_input is hardcoded so we can test against known result values for
        different activation functions
        """
        self.theano_input = T.matrix()
        self.numpy_input = np.array([[-1, 2, -3, 4, 5],
                                     [-1, 2, -3, 4, 5],
                                     [-1, 2, -3, 4, 5],
                                     [-1, 2, -3, 4, 5],
                                     [-1, 2, -3, 4, 5]],
                                    dtype=theano.config.floatX)

    def test_abs(self):
        expected_array = np.array([[1.,  2.,  3.,  4.,  5.],
                                   [1.,  2.,  3.,  4.,  5.],
                                   [1.,  2.,  3.,  4.,  5.],
                                   [1.,  2.,  3.,  4.,  5.],
                                   [1.,  2.,  3.,  4.,  5.]])
        theano_result = A.Abs(self.theano_input).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_relu(self):
        expected_array = np.array([[-0.,  2., -0.,  4.,  5.],
                                   [-0.,  2., -0.,  4.,  5.],
                                   [-0.,  2., -0.,  4.,  5.],
                                   [-0.,  2., -0.,  4.,  5.],
                                   [-0.,  2., -0.,  4.,  5.]])
        theano_result = A.ReLU(self.theano_input).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_elu(self):
        expected_array = np.array([[-0.63212056, 2., -0.95021293, 4., 5.],
                                   [-0.63212056, 2., -0.95021293, 4., 5.],
                                   [-0.63212056, 2., -0.95021293, 4., 5.],
                                   [-0.63212056, 2., -0.95021293, 4., 5.],
                                   [-0.63212056, 2., -0.95021293, 4., 5.]])
        alpha = 1
        theano_result = A.Elu(self.theano_input, alpha).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_sigmoid(self):
        expected_array = np.array([[0.26894142,  0.88079708,  0.04742587,  0.98201379,  0.99330715],
                                   [0.26894142,  0.88079708,  0.04742587,  0.98201379,  0.99330715],
                                   [0.26894142,  0.88079708,  0.04742587,  0.98201379,  0.99330715],
                                   [0.26894142,  0.88079708,  0.04742587,  0.98201379,  0.99330715],
                                   [0.26894142,  0.88079708,  0.04742587,  0.98201379,  0.99330715]])
        theano_result = A.Sigmoid(self.theano_input).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_tanh(self):
        expected_array = np.array([[-0.76159416,  0.96402758, -0.99505475,  0.9993293 ,  0.9999092 ],
                                   [-0.76159416,  0.96402758, -0.99505475,  0.9993293 ,  0.9999092 ],
                                   [-0.76159416,  0.96402758, -0.99505475,  0.9993293 ,  0.9999092 ],
                                   [-0.76159416,  0.96402758, -0.99505475,  0.9993293 ,  0.9999092 ],
                                   [-0.76159416,  0.96402758, -0.99505475,  0.9993293 ,  0.9999092 ]])
        theano_result = A.Tanh(self.theano_input).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_softmax(self):
        expected_array = np.array([[1.74500937e-03,   3.50494502e-02,   2.36161338e-04,
                                    2.58982354e-01,   7.03987026e-01],
                                   [1.74500937e-03,   3.50494502e-02,   2.36161338e-04,
                                    2.58982354e-01,   7.03987026e-01],
                                   [1.74500937e-03,   3.50494502e-02,   2.36161338e-04,
                                    2.58982354e-01,   7.03987026e-01],
                                   [1.74500937e-03,   3.50494502e-02,   2.36161338e-04,
                                    2.58982354e-01,   7.03987026e-01],
                                   [1.74500937e-03,   3.50494502e-02,   2.36161338e-04,
                                    2.58982354e-01,   7.03987026e-01]])
        theano_result = A.Softmax(self.theano_input).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_temperature_softmax(self):
        """
        Utilized np.asarray(np.random.uniform(2, 10, 1), dtype = theano.config.floatX)
        to hardcode a value for t.
        """
        t = np.array([7.94705237])
        expected_array = np.array([[0.1381257,  0.20147445,  0.10739337,  0.25912957,  0.29387691],
                                   [0.1381257,  0.20147445,  0.10739337,  0.25912957,  0.29387691],
                                   [0.1381257,  0.20147445,  0.10739337,  0.25912957,  0.29387691],
                                   [0.1381257,  0.20147445,  0.10739337,  0.25912957,  0.29387691],
                                   [0.1381257,  0.20147445,  0.10739337,  0.25912957,  0.29387691]])
        theano_result = A.Softmax(self.theano_input, temp=t).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))

    def test_squared(self):
        expected_array = np.array([[1., 4., 9., 16., 25.],
                                   [1., 4., 9., 16., 25.],
                                   [1., 4., 9., 16., 25.],
                                   [1., 4., 9., 16., 25.],
                                   [1., 4., 9., 16., 25.]])
        theano_result = A.Squared(self.theano_input).eval({self.theano_input: self.numpy_input})
        self.assertEqual(theano_result.shape, expected_array.shape)
        self.assertTrue(np.allclose(theano_result, expected_array))
