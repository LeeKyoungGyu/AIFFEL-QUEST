import tensorflow as tf
from tensorflow import keras

def _make_deconv_layer(num_deconv_layers):
    seq_model = tf.keras.models.Sequential()
    for _ in range(num_deconv_layers):
        seq_model.add(tf.keras.layers.Conv2DTranspose(256, kernel_size=(4, 4), strides=(2, 2), padding='same'))
        seq_model.add(tf.keras.layers.BatchNormalization())
        seq_model.add(tf.keras.layers.ReLU())
    return seq_model

def SimpleBaseline(input_shape=(256, 256, 3)):
    inputs = keras.Input(shape=input_shape)
    resnet = tf.keras.applications.resnet.ResNet50(include_top=False, weights='imagenet')
    x = resnet(inputs)
    upconv = _make_deconv_layer(3)
    x = upconv(x)
    final_layer = tf.keras.layers.Conv2D(16, kernel_size=(1, 1), padding='same')
    out = final_layer(x)
    model = keras.Model(inputs, out, name='simple_baseline')
    return model