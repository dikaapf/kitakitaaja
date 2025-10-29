from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import DataKependudukan, Daerah, Desa, Kelompok


class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(
      label=_("Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Password"}),
  )
  password2 = forms.CharField(
      label=_("Password Confirmation"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Confirm Password"}),
  )

  class Meta:
    model = User
    fields = ('username', 'email', )

    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control',
          "placeholder": "Username",
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          "placeholder": "Email"
      })
    }


class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(
      label=_("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
  )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        "placeholder": "Email",
    }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "New Password",
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Confirm New Password"
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Old Password"
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "New Password"
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Confirm New Password"
    }), label="Confirm New Password")


class DataKependudukanForm(forms.ModelForm):
    class Meta:
        model = DataKependudukan
        fields = [
            'nik', 'nama_lengkap', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir',
            'daerah', 'desa', 'kelompok', 'alamat_lengkap', 'rt', 'rw',
            'agama', 'status_perkawinan', 'pekerjaan', 'pendidikan_terakhir',
            'nama_ayah', 'nama_ibu', 'nama_pasangan',
            'no_telepon', 'email', 'keterangan', 'foto'
        ]
        widgets = {
            'nik': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan NIK (16 digit)',
                'maxlength': '16'
            }),
            'nama_lengkap': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap'
            }),
            'jenis_kelamin': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tempat_lahir': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan tempat lahir'
            }),
            'tanggal_lahir': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'daerah': forms.Select(attrs={
                'class': 'form-select'
            }),
            'desa': forms.Select(attrs={
                'class': 'form-select'
            }),
            'kelompok': forms.Select(attrs={
                'class': 'form-select'
            }),
            'alamat_lengkap': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat lengkap',
                'rows': 3
            }),
            'rt': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'RT',
                'maxlength': '3'
            }),
            'rw': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'RW',
                'maxlength': '3'
            }),
            'agama': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status_perkawinan': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pekerjaan': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pendidikan_terakhir': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nama_ayah': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama ayah'
            }),
            'nama_ibu': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama ibu'
            }),
            'nama_pasangan': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama pasangan'
            }),
            'no_telepon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nomor telepon'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan email'
            }),
            'keterangan': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan keterangan tambahan',
                'rows': 3
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Memberikan placeholder untuk select field yang kosong
        self.fields['daerah'].empty_label = "Pilih Daerah"
        self.fields['desa'].empty_label = "Pilih Desa"
        self.fields['kelompok'].empty_label = "Pilih Kelompok"
        
        # Set required fields
        required_fields = ['nik', 'nama_lengkap', 'jenis_kelamin', 'tempat_lahir', 
                          'tanggal_lahir', 'daerah', 'desa', 'kelompok', 
                          'alamat_lengkap', 'rt', 'rw', 'agama', 'status_perkawinan', 
                          'pekerjaan', 'pendidikan_terakhir']
        
        for field_name in required_fields:
            self.fields[field_name].required = True
            
        # Add validation messages
        self.fields['nik'].error_messages = {
            'required': 'NIK wajib diisi',
            'unique': 'NIK sudah terdaftar dalam sistem'
        }
        self.fields['nama_lengkap'].error_messages = {
            'required': 'Nama lengkap wajib diisi'
        }

    def clean_nik(self):
        nik = self.cleaned_data.get('nik')
        if nik:
            # Validasi panjang NIK
            if len(nik) != 16:
                raise forms.ValidationError('NIK harus terdiri dari 16 digit')
            # Validasi hanya angka
            if not nik.isdigit():
                raise forms.ValidationError('NIK hanya boleh berisi angka')
        return nik