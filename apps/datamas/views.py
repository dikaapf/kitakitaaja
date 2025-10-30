from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from apps.datamas.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm, DataKependudukanForm
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import DataKependudukan, Daerah, Desa, Kelompok
from django import forms

# Dashboard
def default(request):
  context = {
    'parent': 'dashboard',
    'segment': 'default'
  }
  return render(request, 'pages/dashboards/default.html', context)

# Lihat Data
def messages(request):
  context = {
    'parent': 'pages',
    'segment': 'messages'
  }
  return render(request, 'pages/pages/messages.html', context)

def widgets(request):
  context = {
    'parent': 'pages',
    'segment': 'widgets'
  }
  return render(request, 'pages/pages/widgets.html', context)

def charts_page(request):
  context = {
    'parent': 'pages',
    'segment': 'charts'
  }
  return render(request, 'pages/pages/charts.html', context)

def sweet_alerts(request):
  context = {
    'parent': 'pages',
    'segment': 'sweet_alerts'
  }
  return render(request, 'pages/pages/sweet-alerts.html', context)

def notifications(request):
  context = {
    'parent': 'pages',
    'segment': 'notifications'
  }
  return render(request, 'pages/pages/notifications.html', context)

def pricing_page(request):
  return render(request, 'pages/pages/pricing-page.html')

def rtl(request):
  return render(request, 'pages/pages/rtl-page.html')

# Pages -> Profile
def profile_overview(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'profile',
    'segment': 'profile_overview'
  }
  return render(request, 'pages/profile/overview.html', context)

def teams(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'profile',
    'segment': 'teams'
  }
  return render(request, 'pages/profile/teams.html', context)

def projects(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'profile',
    'segment': 'projects'
  }
  return render(request, 'pages/profile/projects.html', context)

# Pages -> Users
def reports(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'users',
    'segment': 'reports'
  }
  return render(request, 'pages/users/reports.html', context)

def new_user(request):
  context = {
    'parent': 'pages',
    'sub_parent': 'users',
    'segment': 'new_user'
  }
  return render(request, 'pages/users/new-user.html', context)

# Pages -> Accounts
def settings(request):
  context = {
    'parent': 'accounts',
    'segment': 'settings'
  }
  return render(request, 'pages/account/settings.html', context)

def billing(request):
  context = {
    'parent': 'accounts',
    'segment': 'billing'
  }
  return render(request, 'pages/account/billing.html', context)

def invoice(request):
  context = {
    'parent': 'accounts',
    'segment': 'invoice'
  }
  return render(request, 'pages/account/invoice.html', context)

def security(request):
  context = {
    'parent': 'accounts',
    'segment': 'security'
  }
  return render(request, 'pages/account/security.html', context)

# Pages -> Projects
def general(request):
  context = {
    'parent': 'projects',
    'segment': 'general'
  }
  return render(request, 'pages/projects/general.html', context)

def timeline(request):
  context = {
    'parent': 'projects',
    'segment': 'timeline'
  }
  return render(request, 'pages/projects/timeline.html', context)

def new_project(request):
  context = {
    'parent': 'projects',
    'segment': 'new_project'
  }
  return render(request, 'pages/projects/new-project.html', context)

# Applications
def kanban(request):
  context = {
    'parent': 'applications',
    'segment': 'kanban'
  }
  return render(request, 'pages/applications/kanban.html', context)

def wizard(request):
  context = {
    'parent': 'applications',
    'segment': 'wizard'
  }
  return render(request, 'pages/applications/wizard.html', context)

def datatables(request):
  context = {
    'parent': 'applications',
    'segment': 'datatables'
  }
  return render(request, 'pages/applications/datatables.html', context)

def calendar(request):
  context = {
    'parent': 'applications',
    'segment': 'calendar'
  }
  return render(request, 'pages/applications/calendar.html', context)

def analytics(request):
  context = {
    'parent': 'applications',
    'segment': 'analytics'
  }
  return render(request, 'pages/applications/analytics.html', context)

# Ecommerce
def overview(request):
  context = {
    'parent': 'ecommerce',
    'segment': 'overview'
  }
  return render(request, 'pages/ecommerce/overview.html', context)

def referral(request):
  context = {
    'parent': 'ecommerce',
    'segment': 'referral'
  }
  return render(request, 'pages/ecommerce/referral.html', context)

# Ecommerce -> Products
def new_product(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'new_product'
  }
  return render(request, 'pages/ecommerce/products/new-product.html', context)

def edit_product(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'edit_product'
  }
  return render(request, 'pages/ecommerce/products/edit-product.html', context)

def product_page(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'product_page'
  }
  return render(request, 'pages/ecommerce/products/product-page.html', context)

def products_list(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'products',
    'segment': 'products_list'
  }
  return render(request, 'pages/ecommerce/products/products-list.html', context)

# Ecommerce -> Orders
def order_list(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'orders',
    'segment': 'order_list'
  }
  return render(request, 'pages/ecommerce/orders/list.html', context)

def order_details(request):
  context = {
    'parent': 'ecommerce',
    'sub_parent': 'orders',
    'segment': 'order_details'
  }
  return render(request, 'pages/ecommerce/orders/details.html', context)

# Team
def team_messages(request):
  context = {
    'parent': 'team',
    'segment': 'team_messages'
  }
  return render(request, 'pages/team/messages.html', context)

def team_new_user(request):
  context = {
    'parent': 'team',
    'segment': 'team_new_user'
  }
  return render(request, 'pages/team/new-user.html', context)

def team_overview(request):
  context = {
    'parent': 'team',
    'segment': 'team_overview'
  }
  return render(request, 'pages/team/overview.html', context)

def team_projects(request):
  context = {
    'parent': 'team',
    'segment': 'team_projects'
  }
  return render(request, 'pages/team/projects.html', context)

def team_reports(request):
  context = {
    'parent': 'team',
    'segment': 'team_reports'
  }
  return render(request, 'pages/team/reports.html', context)

def team_teams(request):
  context = {
    'parent': 'team',
    'segment': 'team_teams'
  }
  return render(request, 'pages/team/teams.html', context)

# Authentication -> Register
def basic_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/accounts/login/illustration-login/')
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'authentication/signup/basic.html', context)

def cover_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/accounts/login/cover-login/')
  else:
    form = RegistrationForm()

  context = {'form': form}
  return render(request, 'authentication/signup/cover.html', context)

def illustration_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/accounts/login/illustration-login/')
  else:
    form = RegistrationForm()

  context = {'form': form}
  return render(request, 'authentication/signup/illustration.html', context)

# Authentication -> Login
class IllustrationLoginView(LoginView):
  template_name = 'authentication/signin/illustration.html'
  form_class = LoginForm

# Authentication -> Reset
class IllustrationResetView(PasswordResetView):
  template_name = 'authentication/reset/illustration.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'authentication/reset-confirm/basic.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'authentication/change/basic.html'
  form_class = UserPasswordChangeForm

# Authentication -> Lock
def illustration_lock(request):
  return render(request, 'authentication/lock/illustration.html')

# Authentication -> Verification
def illustration_verification(request):
  return render(request, 'authentication/verification/illustration.html')

# Error
def error_404(request,exception=None ):
  return render(request, 'authentication/error/404.html')

def error_500(request, exception=None):
  return render(request, 'authentication/error/500.html')

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/illustration-login/')


# ===================== Data Master CRUD Views =====================

@login_required
def datakependudukan_list(request):
    """View untuk menampilkan daftar data master dengan fitur pencarian dan pagination"""
    search_query = request.GET.get('search', '')
    daerah_filter = request.GET.get('daerah', '')
    desa_filter = request.GET.get('desa', '')
    kelompok_filter = request.GET.get('kelompok', '')
    
    # Query dasar
    data_list = DataKependudukan.objects.all()
    
    # Filter berdasarkan pencarian
    if search_query:
        data_list = data_list.filter(
            Q(nama_lengkap__icontains=search_query) |
            Q(nik__icontains=search_query) |
            Q(tempat_lahir__icontains=search_query) |
            Q(alamat_lengkap__icontains=search_query)
        )
    
    # Filter berdasarkan daerah
    if daerah_filter:
        data_list = data_list.filter(daerah_id=daerah_filter)
    
    # Filter berdasarkan desa
    if desa_filter:
        data_list = data_list.filter(desa_id=desa_filter)
    
    # Filter berdasarkan kelompok
    if kelompok_filter:
        data_list = data_list.filter(kelompok_id=kelompok_filter)
    
    # Pagination
    paginator = Paginator(data_list, 20)  # 20 data per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Data untuk filter dropdown
    daerah_list = Daerah.objects.all()
    desa_list = Desa.objects.all()
    kelompok_list = Kelompok.objects.all()
    
    context = {
        'parent': 'datamas',
        'segment': 'datamaster_list',
        'page_obj': page_obj,
        'search_query': search_query,
        'daerah_filter': daerah_filter,
        'desa_filter': desa_filter,
        'kelompok_filter': kelompok_filter,
        'daerah_list': daerah_list,
        'desa_list': desa_list,
        'kelompok_list': kelompok_list,
        'total_data': data_list.count(),
    }
    return render(request, 'datamas/datamaster_list.html', context)


@login_required
def datakependudukan_detail(request, pk):
    """View untuk menampilkan detail data master"""
    data = get_object_or_404(DataKependudukan, pk=pk)
    context = {
        'parent': 'datamas',
        'segment': 'datamaster_detail',
        'data': data,
    }
    return render(request, 'datamas/datamaster_detail.html', context)


@login_required
def datakependudukan_create(request):
    """View untuk membuat data master baru"""
    if request.method == 'POST':
        form = DataKependudukanForm(request.POST, request.FILES)
        # Sembunyikan RT, RW, dan Agama tanpa ubah template
        for fname in ['rt', 'rw', 'agama']:
            if fname in form.fields:
                form.fields[fname].required = False
        if 'rt' in form.fields:
            form.fields['rt'].widget = forms.HiddenInput()
            form.fields['rt'].label = ''
            form.fields['rt'].initial = '000'
        if 'rw' in form.fields:
            form.fields['rw'].widget = forms.HiddenInput()
            form.fields['rw'].label = ''
            form.fields['rw'].initial = '000'
        if 'agama' in form.fields:
            form.fields['agama'].widget = forms.HiddenInput()
            form.fields['agama'].label = ''
            form.fields['agama'].initial = 'lainnya'

        if form.is_valid():
            data = form.save(commit=False)
            # Pastikan default jika tidak ada input dari form
            if not getattr(data, 'agama', None):
                data.agama = 'lainnya'
            data.rt = data.rt or '000'
            data.rw = data.rw or '000'
            data.created_by = request.user
            data.save()
            messages.success(request, f'Data Master {data.nama_lengkap} berhasil ditambahkan!')
            return redirect('datamaster_detail', pk=data.pk)
    else:
        form = DataKependudukanForm()
        # Sembunyikan RT, RW, dan Agama tanpa ubah template
        for fname in ['rt', 'rw', 'agama']:
            if fname in form.fields:
                form.fields[fname].required = False
        if 'rt' in form.fields:
            form.fields['rt'].widget = forms.HiddenInput()
            form.fields['rt'].label = ''
            form.fields['rt'].initial = '000'
        if 'rw' in form.fields:
            form.fields['rw'].widget = forms.HiddenInput()
            form.fields['rw'].label = ''
            form.fields['rw'].initial = '000'
        if 'agama' in form.fields:
            form.fields['agama'].widget = forms.HiddenInput()
            form.fields['agama'].label = ''
            form.fields['agama'].initial = 'lainnya'

    context = {
        'parent': 'datamas',
        'segment': 'datamaster_create',
        'form': form,
    }
    return render(request, 'datamas/datamaster_form.html', context)


@login_required
def datakependudukan_update(request, pk):
    """View untuk mengupdate data master"""
    data = get_object_or_404(DataKependudukan, pk=pk)
    
    if request.method == 'POST':
        form = DataKependudukanForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Data Master {data.nama_lengkap} berhasil diupdate!')
            return redirect('datamaster_detail', pk=data.pk)
    else:
        form = DataKependudukanForm(instance=data)
    
    context = {
        'parent': 'datamas',
        'segment': 'datamaster_update',
        'form': form,
        'data': data,
        'is_update': True,
    }
    return render(request, 'datamas/datamaster_form.html', context)


@login_required
def datakependudukan_delete(request, pk):
    """View untuk menghapus data master"""
    data = get_object_or_404(DataKependudukan, pk=pk)
    
    if request.method == 'POST':
        nama = data.nama_lengkap
        data.delete()
        messages.success(request, f'Data Master {nama} berhasil dihapus!')
        return redirect('datamaster_list')
    
    context = {
        'parent': 'datamas',
        'segment': 'datamaster_delete',
        'data': data,
    }
    return render(request, 'datamas/datamaster_confirm_delete.html', context)


# ===================== AJAX Views untuk Dynamic Dropdown =====================

def get_desa_by_daerah(request):
    """AJAX view untuk mendapatkan desa berdasarkan daerah"""
    daerah_id = request.GET.get('daerah_id')
    desa_list = []
    
    if daerah_id:
        desa_queryset = Desa.objects.filter(daerah_id=daerah_id)
        desa_list = [{'id': desa.id_desa, 'name': desa.nama_desa} for desa in desa_queryset]
    
    return JsonResponse({'desa_list': desa_list})


def get_daerah_by_desa(request):
    """AJAX view untuk mendapatkan daerah berdasarkan desa"""
    desa_id = request.GET.get('desa_id')
    daerah_id = None
    
    if desa_id:
        try:
            desa = Desa.objects.get(id_desa=desa_id)
            daerah_id = desa.id_daerah.id_daerah if desa.id_daerah else None
        except Desa.DoesNotExist:
            pass
    
    return JsonResponse({'daerah_id': daerah_id})


def get_kelompok_by_desa(request):
    """AJAX view untuk mendapatkan kelompok berdasarkan desa"""
    desa_id = request.GET.get('desa_id')
    kelompok_list = []
    
    if desa_id:
        kelompok_queryset = Kelompok.objects.filter(desa_id=desa_id)
        kelompok_list = [{'id': kelompok.id_kel, 'name': kelompok.nama_kel} for kelompok in kelompok_queryset]
    
    return JsonResponse({'kelompok_list': kelompok_list})


# ===================== Data Master Views =====================

@login_required
def master_daerah(request):
    """View untuk mengelola master data daerah"""
    # Handle form submission
    if request.method == 'POST':
        action = request.POST.get('action', 'add')
        nama_daerah = request.POST.get('nama_daerah')
        
        if action == 'edit':
            # Edit existing daerah
            id_daerah = request.POST.get('id_daerah')
            if id_daerah and nama_daerah:
                try:
                    daerah = Daerah.objects.get(id_daerah=id_daerah)
                    daerah.nama_daerah = nama_daerah
                    daerah.save()
                    print(f"Daerah updated: {id_daerah} - {nama_daerah}")
                except Exception as e:
                    print(f"Error updating daerah: {e}")
                return redirect('master_daerah')
        elif action == 'delete':
            # Delete existing daerah
            id_daerah = request.POST.get('id_daerah')
            if id_daerah:
                try:
                    daerah = Daerah.objects.get(id_daerah=id_daerah)
                    nama = daerah.nama_daerah
                    daerah.delete()
                    print(f"Daerah deleted: {id_daerah} - {nama}")
                except Exception as e:
                    print(f"Error deleting daerah: {e}")
                return redirect('master_daerah')
        else:
            # Add new daerah
            if nama_daerah:
                Daerah.objects.create(nama_daerah=nama_daerah)
                return redirect('master_daerah')
    
    # Get search query
    search_query = request.GET.get('search', '')
    
    # Filter daerah list
    daerah_list = Daerah.objects.all()
    if search_query:
        daerah_list = daerah_list.filter(nama_daerah__icontains=search_query)
    
    context = {
        'parent': 'datamas',
        'segment': 'master_daerah',
        'daerah_list': daerah_list,
        'search_query': search_query,
    }
    return render(request, 'datamas/master_daerah.html', context)


@login_required
def master_desa(request):
    """View untuk mengelola master data desa"""
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            nama_desa = request.POST.get('nama_desa')
            id_daerah = request.POST.get('id_daerah')
            try:
                daerah = Daerah.objects.get(id_daerah=id_daerah)
                Desa.objects.create(nama_desa=nama_desa, id_daerah=daerah)
                messages.success(request, f'Desa {nama_desa} berhasil ditambahkan')
            except Daerah.DoesNotExist:
                messages.error(request, 'Daerah tidak ditemukan')
            except Exception as e:
                messages.error(request, f'Gagal menambahkan desa: {str(e)}')
                
        elif action == 'edit':
            id_desa = request.POST.get('id_desa')
            nama_desa = request.POST.get('nama_desa')
            id_daerah = request.POST.get('id_daerah')
            try:
                desa = Desa.objects.get(id_desa=id_desa)
                daerah = Daerah.objects.get(id_daerah=id_daerah)
                desa.nama_desa = nama_desa
                desa.id_daerah = daerah
                desa.save()
                messages.success(request, f'Desa berhasil diperbarui menjadi {nama_desa}')
            except Desa.DoesNotExist:
                messages.error(request, 'Desa tidak ditemukan')
            except Daerah.DoesNotExist:
                messages.error(request, 'Daerah tidak ditemukan')
            except Exception as e:
                messages.error(request, f'Gagal memperbarui desa: {str(e)}')
                
        elif action == 'delete':
            id_desa = request.POST.get('id_desa')
            try:
                desa = Desa.objects.get(id_desa=id_desa)
                nama = desa.nama_desa
                desa.delete()
                messages.success(request, f'Desa {nama} berhasil dihapus')
            except Desa.DoesNotExist:
                messages.error(request, 'Desa tidak ditemukan')
            except Exception as e:
                messages.error(request, f'Gagal menghapus desa: {str(e)}')
    
    # Filter berdasarkan pencarian jika ada
    search_query = request.GET.get('search', '')
    if search_query:
        desa_list = Desa.objects.filter(nama_desa__icontains=search_query)
    else:
        desa_list = Desa.objects.all()
    
    # Ambil daftar daerah untuk dropdown
    daerah_list = Daerah.objects.all()
        
    context = {
        'parent': 'datamas',
        'segment': 'master_desa',
        'desa_list': desa_list,
        'daerah_list': daerah_list,
        'search_query': search_query,
    }
    return render(request, 'datamas/master_desa.html', context)


@login_required
def master_kelompok(request):
    """View untuk mengelola master data kelompok"""
    # Filter berdasarkan pencarian jika ada
    search_query = request.GET.get('search', '')
    if search_query:
        kelompok_list = Kelompok.objects.filter(nama_kel__icontains=search_query)
    else:
        kelompok_list = Kelompok.objects.all()
        
    # Handle POST requests for add, edit, delete
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            nama_kelompok = request.POST.get('nama_kelompok')
            try:
                Kelompok.objects.create(nama_kel=nama_kelompok)
                messages.success(request, f"Kelompok '{nama_kelompok}' berhasil ditambahkan.")
            except Exception as e:
                messages.error(request, f"Gagal menambahkan kelompok: {str(e)}")
                
        elif action == 'edit':
            id_kelompok = request.POST.get('id_kelompok')
            nama_kelompok = request.POST.get('nama_kelompok')
            try:
                kelompok = Kelompok.objects.get(id_kel=id_kelompok)
                kelompok.nama_kel = nama_kelompok
                kelompok.save()
                messages.success(request, f"Kelompok berhasil diperbarui menjadi '{nama_kelompok}'.")
            except Kelompok.DoesNotExist:
                messages.error(request, "Kelompok tidak ditemukan.")
            except Exception as e:
                messages.error(request, f"Gagal memperbarui kelompok: {str(e)}")
                
        elif action == 'delete':
            id_kelompok = request.POST.get('id_kelompok')
            try:
                kelompok = Kelompok.objects.get(id_kel=id_kelompok)
                nama = kelompok.nama_kel
                kelompok.delete()
                messages.success(request, f"Kelompok '{nama}' berhasil dihapus.")
            except Kelompok.DoesNotExist:
                messages.error(request, "Kelompok tidak ditemukan.")
            except Exception as e:
                messages.error(request, f"Gagal menghapus kelompok: {str(e)}")
    
    # Ambil data daerah untuk dropdown
    daerah_list = Daerah.objects.all()
    # Ambil data desa untuk dropdown
    desa_list = Desa.objects.all()
    
    context = {
        'parent': 'datamas',
        'segment': 'master_kelompok',
        'kelompok_list': kelompok_list,
        'search_query': search_query,
        'daerah_list': daerah_list,
        'desa_list': desa_list,
    }
    return render(request, 'datamas/master_kelompok.html', context)