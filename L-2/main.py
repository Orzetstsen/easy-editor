from PyQt5.QtWidgets import (
    QApplication, QWidget,
QFileDialog, QLabel, QListWidget,
QHBoxLayout, QVBoxLayout,
QPushButton, QInputDialog
)
import os

from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "modified/"
        
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(self.dir,self.filename)
        self.image = Image.open(image_path)
        
    def showImage(self, path):
        lbl_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lbl_image.width(), lbl_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lbl_image.setPixmap(pixmapimage)
        lbl_image.show()

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_detail(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_emboss(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_edge_enhance(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
    def do_flip2(self):
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
                
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
        
    def do_resize(self):
        size = QInputDialog.getText(win, "Resize image", "Width, Height")
        x,y = (size[0].replace("'","")).split(",")
        print(x, y)
        self.image = self.image.resize((int(x.strip()), int(y.strip())))
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
        
app = QApplication([])
win = QWidget()

win.resize(700,500)
win.setWindowTitle("Easy editor")

btn_dir  = QPushButton("Open folder")
btn_left  = QPushButton("Left")
btn_right  = QPushButton("Right")
btn_bw  = QPushButton("B/W")
btn_sharp  = QPushButton("Sharp")
btn_blur = QPushButton("Blur")
btn_contour = QPushButton("Contour")
btn_detail = QPushButton("Detail")
btn_edge_enhance = QPushButton("Edge enhance")
btn_smooth = QPushButton("Smooth")
btn_emboss = QPushButton("Emboss")
btn_resize = QPushButton("Resize image")
btn_flip = QPushButton("Flip(LF,RT)")
btn_flip2 = QPushButton("Flip(TP,BTM)")


lbl_image = QLabel()
lw_files = QListWidget()

row_3 = QHBoxLayout()
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()


row_1.addWidget(btn_left)
row_1.addWidget(btn_right)
row_1.addWidget(btn_sharp)
row_1.addWidget(btn_bw)
row_1.addWidget(btn_flip)
row_1.addWidget(btn_flip2)
row_1.addWidget(btn_blur)
row_3.addWidget(btn_detail)
row_3.addWidget(btn_emboss)
row_3.addWidget(btn_edge_enhance)
row_3.addWidget(btn_smooth)
row_3.addWidget(btn_contour)
row_3.addWidget(btn_resize)

col_1.addWidget(btn_dir)
col_1.addWidget(lw_files)

col_2.addWidget(lbl_image,95)
col_2.addLayout(row_1)
col_2.addLayout(row_3)

row_2.addLayout(col_1,20)
row_2.addLayout(col_2,80)

win.setLayout(row_2)
win.show()

workdir = ""

def filter(files,extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endswith(ext):
                result.append(filename)
    return result


def chose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
    
def show_filename_list():
    extentions = ['.jpg', ".png", ".jpeg", ".gif", ".bmp"]
    chose_workdir()
    filenames = filter(os.listdir(workdir), extentions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
        
        
workimage = ImageProcessor()


def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir,filename)
        image_path = os.path.join(workimage.dir,
                                  workimage.filename)
        workimage.showImage(image_path)


btn_dir.clicked.connect(show_filename_list)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)
btn_flip2.clicked.connect(workimage.do_flip2)
btn_sharp.clicked.connect(workimage.do_sharp)
btn_blur.clicked.connect(workimage.do_blur)
btn_contour.clicked.connect(workimage.do_contour)
btn_detail.clicked.connect(workimage.do_detail)
btn_emboss.clicked.connect(workimage.do_emboss)
btn_edge_enhance.clicked.connect(workimage.do_edge_enhance)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_resize.clicked.connect(workimage.do_resize)

btn_bw.clicked.connect(workimage.do_bw)
lw_files.currentRowChanged.connect(showChosenImage)
app.exec_()




