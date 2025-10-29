import json
from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField

ROLE_CHOICES = (
    ('superadmin'  , 'Super Admin'),
    ('admin'  , 'Admin'),
    ('user'  , 'User'),
)

# Create your models here.
class Daerah(models.Model):
    id_daerah    = models.AutoField(primary_key=True)
    nama_daerah  = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nama_daerah
    
class Desa(models.Model):
    id_desa    = models.AutoField(primary_key=True)
    nama_desa  = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nama_desa
    
class Kelompok(models.Model):
    id_kel    = models.AutoField(primary_key=True)
    nama_kel  = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nama_kel

def avatar_with_id(instance, filename):
    return "{}/avatar/{}".format(f"{instance.user.id}", filename)

def convert_to_quill():
    converted_data = {
        "delta": "",
        "html": "Keterangan atau catatan dari data",
    }
    return json.dumps(converted_data)


class DataMas(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    role      = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    full_nama = models.CharField(max_length=255, null=True, blank=True)
    gender    = models.CharField(max_length=255, null=True, blank=True)
    no_hp     = models.CharField(max_length=255, null=True, blank=True)
    email     = models.CharField(max_length=255, null=True, blank=True)
    foto      = models.ImageField(upload_to=avatar_with_id, null=True, blank=True)
    keterangan       = QuillField(default=convert_to_quill())


    def __str__(self):
        return self.user.username

# Pilihan untuk jenis kelamin
GENDER_CHOICES = (
    ('L', 'Laki-laki'),
    ('P', 'Perempuan'),
)

# Pilihan untuk status perkawinan
STATUS_KAWIN_CHOICES = (
    ('belum_kawin', 'Belum Kawin'),
    ('kawin', 'Kawin'),
    ('cerai_hidup', 'Cerai Hidup'),
    ('cerai_mati', 'Cerai Mati'),
)

# Pilihan untuk agama
AGAMA_CHOICES = (
    ('islam', 'Islam'),
    ('kristen', 'Kristen'),
    ('katolik', 'Katolik'),
    ('hindu', 'Hindu'),
    ('buddha', 'Buddha'),
    ('khonghucu', 'Khonghucu'),
    ('lainnya', 'Lainnya'),
)

# Pilihan untuk pendidikan
PENDIDIKAN_CHOICES = (
    ('tidak_sekolah', 'Tidak/Belum Sekolah'),
    ('tidak_tamat_sd', 'Tidak Tamat SD/Sederajat'),
    ('tamat_sd', 'Tamat SD/Sederajat'),
    ('tamat_smp', 'SLTP/Sederajat'),
    ('tamat_sma', 'SLTA/Sederajat'),
    ('diploma_i', 'Diploma I/II'),
    ('akademi', 'Akademi/Diploma III/S.Muda'),
    ('diploma_iv', 'Diploma IV/Strata I'),
    ('strata_ii', 'Strata II'),
    ('strata_iii', 'Strata III'),
)

# Pilihan untuk pekerjaan
PEKERJAAN_CHOICES = (
    ('belum_bekerja', 'Belum/Tidak Bekerja'),
    ('mengurus_rumah_tangga', 'Mengurus Rumah Tangga'),
    ('pelajar', 'Pelajar/Mahasiswa'),
    ('pensiunan', 'Pensiunan'),
    ('pegawai_negeri', 'Pegawai Negeri Sipil'),
    ('tni', 'TNI'),
    ('kepolisian', 'KEPOLISIAN'),
    ('perdagangan', 'Perdagangan'),
    ('petani', 'Petani/Pekebun'),
    ('peternak', 'Peternak'),
    ('nelayan', 'Nelayan/Perikanan'),
    ('industri', 'Industri'),
    ('konstruksi', 'Konstruksi'),
    ('transportasi', 'Transportasi'),
    ('karyawan_swasta', 'Karyawan Swasta'),
    ('karyawan_bumn', 'Karyawan BUMN'),
    ('karyawan_bumd', 'Karyawan BUMD'),
    ('karyawan_honorer', 'Karyawan Honorer'),
    ('buruh_harian_lepas', 'Buruh Harian Lepas'),
    ('buruh_tani', 'Buruh Tani/Perkebunan'),
    ('buruh_nelayan', 'Buruh Nelayan/Perikanan'),
    ('buruh_peternakan', 'Buruh Peternakan'),
    ('pembantu_rumah_tangga', 'Pembantu Rumah Tangga'),
    ('tukang_cukur', 'Tukang Cukur'),
    ('tukang_listrik', 'Tukang Listrik'),
    ('tukang_batu', 'Tukang Batu'),
    ('tukang_kayu', 'Tukang Kayu'),
    ('tukang_sol_sepatu', 'Tukang Sol Sepatu'),
    ('tukang_las', 'Tukang Las/Pandai Besi'),
    ('tukang_jahit', 'Tukang Jahit'),
    ('tukang_gigi', 'Tukang Gigi'),
    ('penata_rias', 'Penata Rias'),
    ('penata_busana', 'Penata Busana'),
    ('penata_rambut', 'Penata Rambut'),
    ('mekanik', 'Mekanik'),
    ('seniman', 'Seniman'),
    ('tabib', 'Tabib'),
    ('paraji', 'Paraji'),
    ('perancang_busana', 'Perancang Busana'),
    ('penterjemah', 'Penterjemah'),
    ('imam_masjid', 'Imam Masjid'),
    ('pendeta', 'Pendeta'),
    ('pastor', 'Pastor'),
    ('wartawan', 'Wartawan'),
    ('ustadz', 'Ustadz/Mubaligh'),
    ('juru_masak', 'Juru Masak'),
    ('promotor_acara', 'Promotor Acara'),
    ('anggota_dpr_ri', 'Anggota DPR-RI'),
    ('anggota_dpd', 'Anggota DPD'),
    ('anggota_bpk', 'Anggota BPK'),
    ('presiden', 'Presiden'),
    ('wakil_presiden', 'Wakil Presiden'),
    ('anggota_mahkamah_konstitusi', 'Anggota Mahkamah Konstitusi'),
    ('anggota_kabinet', 'Anggota Kabinet Kementerian'),
    ('duta_besar', 'Duta Besar'),
    ('gubernur', 'Gubernur'),
    ('wakil_gubernur', 'Wakil Gubernur'),
    ('bupati', 'Bupati'),
    ('wakil_bupati', 'Wakil Bupati'),
    ('walikota', 'Walikota'),
    ('wakil_walikota', 'Wakil Walikota'),
    ('anggota_dprd_provinsi', 'Anggota DPRD Provinsi'),
    ('anggota_dprd_kabupaten', 'Anggota DPRD Kabupaten/Kota'),
    ('dosen', 'Dosen'),
    ('guru', 'Guru'),
    ('pilot', 'Pilot'),
    ('pengacara', 'Pengacara'),
    ('notaris', 'Notaris'),
    ('arsitek', 'Arsitek'),
    ('akuntan', 'Akuntan'),
    ('konsultan', 'Konsultan'),
    ('dokter', 'Dokter'),
    ('bidan', 'Bidan'),
    ('perawat', 'Perawat'),
    ('apoteker', 'Apoteker'),
    ('psikiater', 'Psikiater/Psikolog'),
    ('penyiar_televisi', 'Penyiar Televisi'),
    ('penyiar_radio', 'Penyiar Radio'),
    ('pelaut', 'Pelaut'),
    ('peneliti', 'Peneliti'),
    ('sopir', 'Sopir'),
    ('pialang', 'Pialang'),
    ('paranormal', 'Paranormal'),
    ('pedagang', 'Pedagang'),
    ('perangkat_desa', 'Perangkat Desa'),
    ('kepala_desa', 'Kepala Desa'),
    ('biarawati', 'Biarawati'),
    ('wiraswasta', 'Wiraswasta'),
    ('lainnya', 'Lainnya'),
)

class DataKependudukan(models.Model):
    # Data Identitas Dasar
    nik = models.CharField(max_length=16, unique=True, verbose_name="NIK")
    nama_lengkap = models.CharField(max_length=255, verbose_name="Nama Lengkap")
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Jenis Kelamin")
    tempat_lahir = models.CharField(max_length=100, verbose_name="Tempat Lahir")
    tanggal_lahir = models.DateField(verbose_name="Tanggal Lahir")
    
    # Data Kependudukan
    daerah = models.ForeignKey(Daerah, on_delete=models.CASCADE, verbose_name="Daerah")
    desa = models.ForeignKey(Desa, on_delete=models.CASCADE, verbose_name="Desa")
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, verbose_name="Kelompok")
    alamat_lengkap = models.TextField(verbose_name="Alamat Lengkap")
    rt = models.CharField(max_length=3, verbose_name="RT")
    rw = models.CharField(max_length=3, verbose_name="RW")
    
    # Data Sosial
    agama = models.CharField(max_length=20, choices=AGAMA_CHOICES, verbose_name="Agama")
    status_perkawinan = models.CharField(max_length=20, choices=STATUS_KAWIN_CHOICES, verbose_name="Status Perkawinan")
    pekerjaan = models.CharField(max_length=50, choices=PEKERJAAN_CHOICES, verbose_name="Pekerjaan")
    pendidikan_terakhir = models.CharField(max_length=30, choices=PENDIDIKAN_CHOICES, verbose_name="Pendidikan Terakhir")
    
    # Data Keluarga
    nama_ayah = models.CharField(max_length=255, verbose_name="Nama Ayah", blank=True, null=True)
    nama_ibu = models.CharField(max_length=255, verbose_name="Nama Ibu", blank=True, null=True)
    nama_pasangan = models.CharField(max_length=255, verbose_name="Nama Pasangan", blank=True, null=True)
    
    # Data Kontak
    no_telepon = models.CharField(max_length=15, verbose_name="No. Telepon", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    
    # Data Tambahan
    keterangan = models.TextField(verbose_name="Keterangan", blank=True, null=True)
    foto = models.ImageField(upload_to='kependudukan/', verbose_name="Foto", blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat Pada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Diupdate Pada")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Dibuat Oleh")
    
    class Meta:
        verbose_name = "Data Kependudukan"
        verbose_name_plural = "Data Kependudukan"
        ordering = ['nama_lengkap']
    
    def __str__(self):
        return f"{self.nama_lengkap} - {self.nik}"
    
    @property
    def umur(self):
        from datetime import date
        today = date.today()
        return today.year - self.tanggal_lahir.year - ((today.month, today.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day))