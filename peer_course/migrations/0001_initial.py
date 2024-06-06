# Generated by Django 2.1.15 on 2024-04-17 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(db_column='display_name', max_length=128, verbose_name='Display Name')),
                ('browsable', models.BooleanField(db_column='browsable', db_index=True, verbose_name='Visible to Students?')),
                ('archived', models.BooleanField(db_column='archived', db_index=True, verbose_name='Archived?')),
                ('stucode', models.CharField(db_column='student_enroll_code', db_index=True, max_length=128, null=True, verbose_name='Student Enroll Code')),
                ('tascode', models.CharField(db_column='ta_enroll_code', db_index=True, max_length=128, null=True, verbose_name='TA Enroll Code')),
                ('instructor_code', models.CharField(db_column='instructor_enroll_code', db_index=True, max_length=128, null=True, verbose_name='Instructor Enroll Code')),
                ('total_late_units', models.IntegerField(blank=True, default=6)),
                ('can_tas_see_reviews', models.BooleanField(default=False)),
                ('enable_independent_pool', models.BooleanField(default=True)),
                ('enable_participation', models.BooleanField(default=False)),
                ('points_upon_participation_in_green_list', models.FloatField(db_column='points_upon_participation_in_green_list', default=10.0, null=True, verbose_name='points_upon_participation_in_green_list')),
                ('points_upon_participation_in_blue_list', models.FloatField(db_column='points_upon_participation_in_blue_list', default=10.0, null=True, verbose_name='points_upon_participation_in_blue_list')),
                ('fraction_of_points_gained_upon_further_participations', models.FloatField(db_column='fraction_of_points_gained_upon_further_participations', default=0.1, null=True, verbose_name='fraction_of_points_gained_upon_further_participations')),
                ('points_upon_participation_in_red_list', models.FloatField(db_column='points_upon_participation_in_red_list', default=0.0, null=True, verbose_name='points_upon_participation_in_red_list')),
                ('points_upon_participation_in_yellow_list', models.FloatField(db_column='points_upon_participation_in_yellow_list', default=0.0, null=True, verbose_name='points_upon_participation_in_yellow_list')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(db_column='role', db_index=True, max_length=128, verbose_name='User Type')),
                ('is_independent', models.BooleanField(db_column='is_independent', db_index=True, default=False, verbose_name='is_independent?')),
                ('time_is_independent_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(blank=True, db_index=True, default=True)),
                ('qualified', models.BooleanField(blank=True, default=True)),
                ('upper_confidence_bound', models.FloatField(db_column='upperconfidencebound', default=1.0, null=True, verbose_name='Upper confidence bound')),
                ('markingload', models.FloatField(db_column='markingload', default=0.0, null=True, verbose_name='Marking Load')),
                ('lower_confidence_bound', models.FloatField(db_column='lowerconfidencebound', default=0.0, null=True, verbose_name='Lower confidence bound')),
                ('hand_up', models.BooleanField(db_column='hand_up', db_index=True, default=False, verbose_name='hand_up')),
                ('hand_up_list_2', models.BooleanField(db_column='hand_up_list_2', db_index=True, default=False, verbose_name='hand_up_list_2')),
                ('hand_up_list_3', models.BooleanField(db_column='hand_up_list_3', db_index=True, default=False, verbose_name='hand_up_list_3')),
                ('hand_up_list_4', models.BooleanField(db_column='hand_up_list_4', db_index=True, default=False, verbose_name='hand_up_list_4')),
                ('spoken', models.BooleanField(db_column='spoken', db_index=True, default=False, verbose_name='spoken')),
                ('time_spoken', models.DateTimeField(db_column='time_spoken', default=django.utils.timezone.now, verbose_name='time_spoken')),
                ('participation_points', models.IntegerField(db_column='participation_points', default=0, null=True, verbose_name='participation_points')),
                ('regular_points', models.IntegerField(db_column='regular_points', default=0, null=True, verbose_name='regular_points')),
                ('first_hand_up', models.BooleanField(db_column='first_hand_up', db_index=True, default=True, verbose_name='first_hand_up')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='peer_course.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_member',
            },
        ),
        migrations.CreateModel(
            name='CourseParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_participated', models.DateTimeField(db_column='time_participated', default=django.utils.timezone.now, verbose_name='time_participated')),
                ('participation_list', models.IntegerField(db_column='participation_list', default=0, null=True, verbose_name='participation_list')),
                ('participation_points_gained', models.IntegerField(db_column='participation_points_gained', default=0, null=True, verbose_name='participation_points_gained')),
                ('spoke_upon_participation', models.BooleanField(db_column='spoke_upon_participation', db_index=True, default=False, verbose_name='spoke_upon_participation')),
                ('count_in_calculations', models.BooleanField(db_column='count_in_calculations', db_index=True, default=True, verbose_name='count_in_calculations')),
                ('real_participation', models.BooleanField(db_column='real_participation', db_index=True, default=True, verbose_name='real_participation')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='peer_course.CourseMember')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='coursemember',
            unique_together={('course', 'user')},
        ),
    ]
