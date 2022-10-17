import glob

import tensorflow as tf

classes = 2
COLORS = ['black', 'red']
SAMPLE_SIZE = (256, 256)

output_size = (1080, 1920)


def load_images(image, mask):
    image = tf.io.read_file(image)
    image = tf.io.decode_jpeg(image)
    image = tf.image.resize(image, output_size)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = image / 255.0

    mask = tf.io.read_file(mask)
    mask = tf.io.decode_png(mask)
    mask = tf.image.resize(mask, output_size)
    mask = tf.image.convert_image_dtype(mask, tf.float32)

    masks = []
    for i in range(classes):
        masks.append(tf.where(tf.equal(mask, float(i)), 1.0, 0.0))

    masks = tf.stack(masks, axis=2)
    masks = tf.reshape(masks, output_size + (classes,))

    return image, masks


def augmentation_images(image, masks):
    random_crop = tf.random.uniform((), 0.3, 1)
    image = tf.image.central_crop(image, random_crop)
    masks = tf.image.central_crop(masks, random_crop)

    random_flip = tf.random.uniform((), 0, 1)
    if random_flip >= 0.5:
        image = tf.image.flip_left_right(image)
        masks = tf.image.flip_left_right(masks)

    image = tf.image.resize(image, SAMPLE_SIZE)
    masks = tf.image.resize(masks, SAMPLE_SIZE)

    return image, masks


images = sorted(glob.glob('C:/Users/glebk/Downloads/src/img/imgre/*.jpeg'))
masks = sorted(glob.glob('C:/Users/glebk/Downloads/src/masks_machine/*.png'))

images_dataset = tf.data.Dataset.from_tensor_slices(images)
masks_dataset = tf.data.Dataset.from_tensor_slices(masks)
print(images)
print(images_dataset)