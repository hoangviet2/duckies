import wget
import tarfile
def run():
    url = "https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz"
    filename = wget.download(url)
    my_tar = tarfile.open('./s2v_reddit_2015_md.tar.gz')
# extract the tar file
    my_tar.extractall()
# closing the file object
    my_tar.close()
    print(filename)
    print("HI")
run()