from PIL import Image

def main():
    number = 37
    for number in range(37,48):
        img = Image.open("modernbig/%d.jpg" % number)

        w5 = (img.size[0] // 100) * 5
        h5 = (img.size[1] // 100) * 5
        croped = img.crop(
            (
                w5,
                h5,
                img.size[0] - w5,
                img.size[1] - h5
            )
        )

        croped.save("modern-big/%d.jpg" % number)
main()