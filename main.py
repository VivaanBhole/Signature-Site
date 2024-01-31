import cv2 as cv
import numpy as np
import streamlit as st

img = cv.imread("sign.jpg", cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (0, 0), fx=.3, fy=.3)


def change_color(hex, img):
    r, g, b = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r
    return img


def threshhold(t, img):
    ret, img = cv.threshold(img, t, 255, cv.THRESH_BINARY)

    height, width = img.shape

    rgba = cv.cvtColor(img, cv.COLOR_RGB2RGBA)
    rgba[:, :, 3] = 255 - rgba[:, :, 2]
    img = rgba
    return img


img = threshhold(100, img)


st.image(img, caption='this is my signature', channels='RGBA')
color = st.color_picker('Pen Color')
img = change_color(color, img)

