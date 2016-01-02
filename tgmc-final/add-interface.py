#!/usr/bin/python
import sys
import gtk
import gtk.glade
import gobject
i=0
button={}
buttond={}
cbezone={}
cbestop={}
listzone=gtk.ListStore(gobject.TYPE_STRING)
listzone.set_sort_column_id(0,gtk.SORT_ASCENDING)
liststop=gtk.ListStore(gobject.TYPE_STRING)
liststop.set_sort_column_id(0,gtk.SORT_ASCENDING)
completzone = gtk.EntryCompletion()
completzone.set_model(listzone)
completzone.set_minimum_key_length(1)
completzone.set_text_column(0)
completstop = gtk.EntryCompletion()
completstop.set_model(liststop)
completstop.set_minimum_key_length(1)
completstop.set_text_column(0)


def search(lstore,key):
	ctr=0
	for i in lstore:
		if i[0] == key:
			return True,ctr
		ctr = ctr + 1
	return False
	
class HellowWorldGTK:
	def __init__(self):
		self.wTree = gtk.glade.XML("./add-interface.glade")
		dic = {
			"window1-destroy" : gtk.main_quit,
			"diaclose": self.winclose,
			}
		self.wTree.signal_autoconnect(dic)
		self.btnHelloWorld_clicked(self)

	def btnHelloWorld_clicked(self, widget):
		global i
		global button
		global buttond
		global cbestop
		global cbezone
		if i >0:
			button[i].hide()
			buttond[i].show()
		i = i + 1
		cbezone[i]=gtk.combo_box_entry_new_text()
		cbezone[i].set_model(listzone)
		cbezone[i].child.set_completion(completzone)
		cbestop[i]=gtk.combo_box_entry_new_text()
		cbestop[i].set_model(liststop)
		cbestop[i].child.set_completion(completstop)
		button[i] = gtk.Button(stock=gtk.STOCK_ADD)
		button[i].connect('clicked',self.ins,i)
		buttond[i] = gtk.Button(stock=gtk.STOCK_DELETE)
		buttond[i].connect('clicked',self.dell,i)
		self.wTree.get_widget("table1").attach(cbezone[i],0,1,i,i+1,yoptions=gtk.FILL)
		self.wTree.get_widget("table1").attach(cbestop[i],1,2,i,i+1,yoptions=gtk.FILL)
		self.wTree.get_widget("table1").attach(button[i],2,3,i,i+1,yoptions=gtk.FILL)
		self.wTree.get_widget("table1").attach(buttond[i],2,3,i,i+1,yoptions=gtk.FILL)
		cbezone[i].show()
		cbestop[i].show()
		button[i].show()
		
	def ins(self,widget,i):
		entryzone = cbezone[i].child
		entrystop = cbestop[i].child
		if entryzone.get_text() == '' or entrystop.get_text() == '':
			self.wTree.get_widget("dialog1").show()
			return
		if search(listzone,entryzone.get_text()) == False:
			cbezone[i].append_text(entryzone.get_text())
		if search(liststop,entryzone.get_text()) == False:
			cbestop[i].append_text(entrystop.get_text())
		self.btnHelloWorld_clicked(self)
			
	def dell(self,widget,i):
		astop = search(liststop,cbestop[i].get_active_text())
		iterstop = liststop.get_iter(astop[1])
		liststop.remove(iterstop)
		cbezone[i].hide()
		cbestop[i].hide()
		button[i].hide()
		buttond[i].hide()
	
	def winclose(self,widget):
		self.wTree.get_widget("dialog1").hide()

hwg = HellowWorldGTK()
gtk.main()
