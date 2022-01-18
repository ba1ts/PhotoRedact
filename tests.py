 
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QMessageBox,QListWidget,
 QHBoxLayout, QVBoxLayout,QFileDialog)
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPalette,QIcon, QBrush, QPixmap 
from PIL import Image, ImageFilter
 
app = QApplication([])
win = QWidget()       
win.resize(700, 500)

palette = QPalette()
palette.setBrush(QPalette.Background, QBrush(QPixmap(".\Coupon_2021_03_02_12627-02.png")))
win.setPalette(palette)

win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()
btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_more = QPushButton("Усилить контур")
btn_blur = QPushButton("Заблюрить")
btn_rock = QPushButton("Тиснение")
btn_mini = QPushButton("Понизить качество")
btn_bw = QPushButton("Ч/Б")
btn_shadow = QPushButton("Оставить только контур")
row = QHBoxLayout()         
col1 = QVBoxLayout()         
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95) 
row_tools = QHBoxLayout()
row_tools2 = QHBoxLayout() 
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_more)
row_tools2.addWidget(btn_blur)
row_tools2.addWidget(btn_rock)
row_tools2.addWidget(btn_mini)
row_tools.addWidget(btn_bw)
row_tools2.addWidget(btn_shadow)

col2.addLayout(row_tools)
col2.addLayout(row_tools2)
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
win.show()
workdir = ''
 
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 
def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
 
def showFilenamesList():
   try:
      extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
      chooseWorkdir()
      filenames = filter(os.listdir(workdir), extensions)
 
      lw_files.clear()
      for filename in filenames:
          lw_files.addItem(filename)
   except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Выберите директорию!")
         msg.exec_()
 
btn_dir.clicked.connect(showFilenamesList)
 
class ImageProcessor():
   def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified/"
 
   def loadImage(self, dir, filename):
       ''' при загрузке запоминаем путь и имя файла '''
       self.dir = dir
       self.filename = filename
       image_path = os.path.join(dir, filename)
       self.image = Image.open(image_path)
 
   def do_bw(self):
      try:
         self.image = self.image.convert("L")
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()

   def do_shadow(self):
      try:
         self.image = self.image.filter(ImageFilter.FIND_EDGES)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()

   def do_more(self):
      try:
          self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
          self.saveImage()
          image_path = os.path.join(self.dir, self.save_dir, self.filename)
          self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()

   def do_rock(self):
      try:
         self.image = self.image.filter(ImageFilter.EMBOSS)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()
       
   def do_sharpen(self):
      try:
         self.image = self.image.filter(ImageFilter.SHARPEN)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()
       
   def do_blur(self):
      try:
         self.image = self.image.filter(ImageFilter.BLUR)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()

   def do_mini(self):
      try:
          self.image = self.image.filter(ImageFilter.MinFilter(size=5))
          self.saveImage()
          image_path = os.path.join(self.dir, self.save_dir, self.filename)
          self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()

   def do_mirrored(self):
      try:
         self.image = self.image.rotate(180)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()

   def do_left(self):
      try:
         self.image = self.image.rotate(270)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()
       
   def do_right(self):
      try:
         self.image = self.image.rotate(90)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
      except:
         msg = QMessageBox()
         msg.setWindowTitle("Error!")
         msg.setText("Что то пошло не так...")
         msg.exec_()
 
   def saveImage(self):
       ''' сохраняет копию файла в подпапке '''
       path = os.path.join(self.dir, self.save_dir)
       print(path)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       image_path = os.path.join(path, self.filename)
       self.image.save(image_path)
 
   def showImage(self, path):
       lb_image.hide()
       pixmapimage = QPixmap(path)
       w, h = lb_image.width(), lb_image.height()
       pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
       lb_image.setPixmap(pixmapimage)
       lb_image.show()
 
def showChosenImage():
   if lw_files.currentRow() >= 0:
       filename = lw_files.currentItem().text()
       workimage.loadImage(workdir, filename)
       image_path = os.path.join(workimage.dir, workimage.filename)
       workimage.showImage(image_path)
 
workimage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)
 
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_mirrored)
btn_shadow.clicked.connect(workimage.do_shadow)
btn_blur.clicked.connect(workimage.do_blur)
btn_mini.clicked.connect(workimage.do_mini)
btn_more.clicked.connect(workimage.do_more)
btn_bw.clicked.connect(workimage.do_bw)
btn_rock.clicked.connect(workimage.do_rock)
btn_sharp.clicked.connect(workimage.do_sharpen)

app.exec()
