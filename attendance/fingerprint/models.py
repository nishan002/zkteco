# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ImprAttendanceTable(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    punch_date = models.DateField(blank=True, null=True)
    card_no = models.TextField()
    in_gate_name = models.CharField(max_length=255, blank=True, null=True)
    in_time = models.TimeField(blank=True, null=True)
    out_gate_name = models.CharField(max_length=255, blank=True, null=True)
    out_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    is_validate = models.CharField(max_length=1)
    error_message = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impr_attendance_table'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BatchImportTable(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_import_table'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendance(models.Model):
    contact_id = models.IntegerField()
    card_no = models.TextField()
    punch_date = models.DateField(blank=True, null=True)
    in_gate_name = models.CharField(max_length=255, blank=True, null=True)
    in_time = models.TimeField(blank=True, null=True)
    out_gate_name = models.CharField(max_length=255, blank=True, null=True)
    out_time = models.TimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    contact_type = models.CharField(max_length=7)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contacts(models.Model):
    contact_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    cp_phone_no = models.CharField(max_length=32, blank=True, null=True)
    cp_email = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    education_qualification = models.CharField(max_length=191, blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=191, blank=True, null=True)
    nid = models.CharField(max_length=191, blank=True, null=True)
    guardian_relation = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fathers_name = models.CharField(max_length=255, blank=True, null=True)
    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=194, blank=True, null=True)
    full_name = models.CharField(max_length=191, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    birth_certificate = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=191, blank=True, null=True)
    blood_group = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=191, blank=True, null=True)
    religion_id = models.IntegerField(blank=True, null=True)
    transport_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    admission_date = models.CharField(max_length=255, blank=True, null=True)
    employee_department_id = models.IntegerField(blank=True, null=True)
    employee_designation_id = models.IntegerField(blank=True, null=True)
    employee_joining_date = models.CharField(max_length=255, blank=True, null=True)
    is_trash = models.IntegerField()
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=255, blank=True, null=True)
    fingerprint_card_no = models.TextField(blank=True, null=True)
    fingerprint_card_serial_no = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'
