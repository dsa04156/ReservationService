# Generated by Django 4.2.1 on 2023-06-09 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('business_hour_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('lunch_start_time', models.TimeField(blank=True, null=True)),
                ('lunch_end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'business_hour',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(max_length=30)),
                ('hospital_name', models.CharField(max_length=30)),
                ('friday', models.ForeignKey(blank=True, db_column='friday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
                ('monday', models.ForeignKey(blank=True, db_column='monday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
                ('saturday', models.ForeignKey(blank=True, db_column='saturday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
                ('sunday', models.ForeignKey(blank=True, db_column='sunday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
                ('thursday', models.ForeignKey(blank=True, db_column='thursday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
                ('tuesday', models.ForeignKey(blank=True, db_column='tuesday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
                ('wednesday', models.ForeignKey(blank=True, db_column='wednesday', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.businesshour')),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='NonReimbursement',
            fields=[
                ('non_reimbursement_id', models.AutoField(primary_key=True, serialize=False)),
                ('non_reimbursement_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'non_reimbursement',
            },
        ),
        migrations.CreateModel(
            name='DoctorNonReimbursement',
            fields=[
                ('doctor_non_reimbursement_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_id', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, related_name='doctor_non_reimbursement', to='doctor.doctor')),
                ('non_reimbursement_id', models.ForeignKey(db_column='non_reimbursement_id', on_delete=django.db.models.deletion.CASCADE, related_name='doctor_non_reimbursement', to='doctor.nonreimbursement')),
            ],
            options={
                'db_table': 'doctor_non_reimbursement',
            },
        ),
        migrations.CreateModel(
            name='DoctorDepartment',
            fields=[
                ('doctor_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_id', models.ForeignKey(db_column='department_id', on_delete=django.db.models.deletion.CASCADE, related_name='doctor_department', to='doctor.department')),
                ('doctor_id', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, related_name='doctor_department', to='doctor.doctor')),
            ],
            options={
                'db_table': 'doctor_department',
            },
        ),
    ]
