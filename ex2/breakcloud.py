from cloud import Cloud


def breakcloud(cloud):
    """
    receives 'cloud', an object of type Cloud.
    creates a file with the name 'plain.txt' that stores the current text that is encrypted in the cloud.
    you can use only the Read/Write interfaces of Cloud (do not use its internal variables.)
    """
    plain_text = bytearray()
    i = 0
    while True:
        try:
            plain_text.append(ord(cloud.Write(i, '\x00')) ^ ord(cloud.Read(i)))
        except IndexError:
            break
        i += 1

    with open("plain.txt", "wb") as f:
        f.write(plain_text)


if __name__ == "__main__":
    breakcloud(Cloud('what.txt'))
