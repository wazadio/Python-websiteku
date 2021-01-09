from django import forms



class FormTugas(forms.Form):
	matkul = [
		('Organisasi dan Arsitektur Komputer II', 'Organisasi dan Arsitektur Komputer II'),
		('Praktikum Organisasi dan Arsitektur Komputer II', 'Praktikum Organisasi dan Arsitektur Komputer II'),
		('Perancangan Sistem Tertanam', 'Perancangan Sistem Tertanam'),
		('Rekayasa Sistem Komputer', 'Rekayasa Sistem Komputer'),
		('Keamanan Informasi', 'Keamanan Informasi'),
		('Sistem Cerdas', 'Sistem Cerdas'),
		('Kewirausahaan', 'Kewirausahaan'),
		('Sistem Multimedia', 'Sistem Multimedia'),
		('Pemrosesan Paralel', 'Pemrosesan Paralel'),
	]
	tahun = (2021,)
	Jam = [("01:00","01:00"), ("02:00","02:00"), ("03:00","03:00"), ("04:00","04:00"), 
			("05:00","05:00"), ("06:00","06:00"), ("07:00","07:00"), ("08:00","08:00"), 
			("09:00","09:00"), ("10:00","10:00"), ("11:00","11:00"), ("12:00","12:00"), 
			("13:00","13:00"), ("14:00","14:00"), ("15:00","15:00"), ("16:00","16:00"), 
			("17:00","17:00"), ("18:00","18:00"), ("19:00","19:00"), ("20:00","20:00"), 
			("21:00","21:00"), ("22:00","22:00"), ("23:00","23:00"), ("23:59","23:59"),
	]

	matakuliah = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=matkul)
	deskripsi = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
	deadline = forms.DateField(widget=forms.SelectDateWidget(years=tahun))
	jam = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Jam)
	


	