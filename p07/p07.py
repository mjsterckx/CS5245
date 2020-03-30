import matplotlib.pyplot as plt
import numpy as np


def construct_file_name(lat, lon):
    file_name_prefix = 'USGS_NED_1_'
    file_name_suffix = '_IMG.tif'
    if lat >= 0:
        file_name_prefix += 'n'
    else:
        file_name_prefix += 's'
    file_name_prefix += str(np.abs(lat))
    if lon >= 0:
        file_name_prefix += 'e'
    else:
        file_name_prefix += 'w'
    if np.abs(lon) < 100:
        file_name_prefix += '0'
    file_name_prefix += str(np.abs(lon))
    return file_name_prefix + file_name_suffix


def load_trim_image(lat, lon):
    im = plt.imread(construct_file_name(lat, lon))
    h, w = im.shape
    im = np.delete(im, slice(h - 6, h), 0)
    im = np.delete(im, slice(0, 6), 0)
    im = np.delete(im, slice(w - 6, w), 1)
    im = np.delete(im, slice(0, 6), 1)
    return im


def stitch_four(lat, lon):
    im0 = load_trim_image(lat, lon)
    im1 = load_trim_image(lat - 1, lon)
    im2 = load_trim_image(lat, lon + 1)
    im3 = load_trim_image(lat - 1, lon + 1)
    im01 = np.concatenate((im0, im1), axis=0)
    im23 = np.concatenate((im2, im3), axis=0)
    im0123 = np.concatenate((im23, im01), axis=1)
    return im0123


def get_row(lat, lon_min, num_tiles):
    im = load_trim_image(lat, lon_min)
    for i in range(1, num_tiles):
        im = np.concatenate((im, load_trim_image(lat, lon_min + i)), axis=1)
    return im


def get_tile_grid(lat_max, lon_min, num_lat, num_lon):
    im = get_row(lat_max, lon_min, num_lon)
    for i in range(1, num_lat):
        im = np.concatenate((im, get_row(lat_max - i, lon_min, num_lon)), axis=0)
    plt.imshow(im)
    plt.colorbar()
    plt.show()
    return im


def get_northwest(lat, lon):
    result = (int(np.ceil(lat)), int(np.floor(lon)))
    return result


def get_tile_grid_decimal(northwest, southeast):
    n, w = northwest
    s, e = southeast
    n, w = get_northwest(n, w)
    s, e = get_northwest(s, e)
    return get_tile_grid(n, w, n - s + 1, e - w + 1)


def dec_to_dms(dec):
    dec2 = np.abs(dec)
    degrees = int(np.floor(dec2))
    if dec < 0:
        degrees = - degrees
    minutes = int(np.round((dec2 % 1) * 60))
    seconds = int(np.round((((dec2 % 1) * 60) % 1) * 60))
    return degrees, minutes, seconds


def seconds_to_index(seconds):
    return (3600 - seconds) % 3600


def get_trim(northwest, southeast):
    n, w = northwest
    s, e = southeast
    left = w * 3600 % 3600
    right = 3599 - (e * 3600 % 3600)
    bottom = (s * 3600 % 3600)
    top = 3600 - (n * 3600 % 3600)
    return int(left % 3600), int(right % 3600), int(bottom % 3600), int(top % 3600)


def get_roi(center, n):
    lat, lon = center
    north = lat + n / 3600
    west = lon - n / 3600
    south = lat - n / 3600
    east = lon + n / 3600
    return (north, west), (south, east)


def crop(im, trim):
    left, right, bottom, top = trim
    h, w = im.shape
    image = np.delete(im, slice(h - bottom, h), axis=0)
    image = np.delete(image, slice(0, top), axis=0)
    image = np.delete(image, slice(w - right, w), axis=1)
    image = np.delete(image, slice(0, left), axis=1)
    return image


def get_extent(northwest, southeast):
    n, w = northwest
    s, e = southeast
    return w, e, s, n


def zoom(center, n):
    northwest, southeast = get_roi(center, n)
    im = get_tile_grid_decimal(northwest, southeast)
    im = crop(im, get_trim(northwest, southeast))
    extent = get_extent(northwest, southeast)
    return extent, im
