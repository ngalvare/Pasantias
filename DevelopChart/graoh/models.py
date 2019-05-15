# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GraohGraphmoes(models.Model):
    monto_req = models.FloatField(blank=True, null=True)
    est_oper_equi = models.CharField(max_length=10)
    mes = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'graoh_graphmoes'


class Tblpoint(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tblPoint'


class Tbltmpcorrect(models.Model):
    anio_docu = models.CharField(max_length=15, blank=True, null=True)
    num_ifal = models.CharField(max_length=25, blank=True, null=True)
    desc_repa_emis_ifal = models.CharField(max_length=80, blank=True, null=True)
    desc_fami = models.CharField(max_length=40, blank=True, null=True)
    desc_sist = models.CharField(max_length=60, blank=True, null=True)
    desc_equi = models.CharField(max_length=120, blank=True, null=True)
    desc_depa_emis_ifal = models.CharField(max_length=70, blank=True, null=True)
    desc_depa_ejec_ifal = models.CharField(max_length=50, blank=True, null=True)
    dias_tran_ulmo_ifal = models.IntegerField(blank=True, null=True)
    fech_ing_ifal = models.DateField(blank=True, null=True)
    mes_ing_ifal = models.CharField(max_length=25, blank=True, null=True)
    desc_esta_ifal = models.CharField(max_length=25, blank=True, null=True)
    fech_cier_ifal = models.DateField(blank=True, null=True)
    desc_falla_ifal = models.CharField(max_length=225, blank=True, null=True)
    desc_causa_ifal = models.CharField(max_length=275, blank=True, null=True)
    desc_solu_ifal = models.CharField(max_length=225, blank=True, null=True)
    tipo_falla = models.CharField(max_length=50, blank=True, null=True)
    esta_oper_unid = models.CharField(max_length=45, blank=True, null=True)
    esta_porc_unid = models.CharField(max_length=25, blank=True, null=True)
    esta_oper_sist = models.CharField(max_length=25, blank=True, null=True)
    esta_porc_sist = models.CharField(max_length=25, blank=True, null=True)
    esta_oper_equi = models.CharField(max_length=25, blank=True, null=True)
    esta_porc_equi = models.CharField(max_length=25, blank=True, null=True)
    nume_insp = models.CharField(max_length=25, blank=True, null=True)
    desc_falla_insp = models.CharField(max_length=225, blank=True, null=True)
    desc_causa_insp = models.CharField(max_length=225, blank=True, null=True)
    num_ortr = models.CharField(max_length=25, blank=True, null=True)
    desc_ortr = models.CharField(max_length=225, blank=True, null=True)
    componente = models.CharField(max_length=40, blank=True, null=True)
    fech_ingr_ortr = models.DateField(blank=True, null=True)
    mes_ingr_ortr = models.CharField(max_length=25, blank=True, null=True)
    desc_esta_ortr = models.CharField(max_length=25, blank=True, null=True)
    desc_depa_emis_ortr = models.CharField(max_length=200, blank=True, null=True)
    desc_depa_ejec_ortr = models.CharField(max_length=200, blank=True, null=True)
    fech_cierre_ortr = models.DateField(blank=True, null=True)
    depa_gene_reque = models.CharField(max_length=25, blank=True, null=True)
    nume_reque = models.CharField(max_length=25, blank=True, null=True)
    monto_reque = models.FloatField(blank=True, null=True)
    desc_esta_reque = models.CharField(max_length=25, blank=True, null=True)
    fech_regi_reque = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblTmpCorrect'


class Tbltmpprevent(models.Model):
    anio_docu = models.CharField(max_length=15, blank=True, null=True)
    num_ifal = models.CharField(max_length=25, blank=True, null=True)
    desc_repa_emis_ifal = models.CharField(max_length=80, blank=True, null=True)
    desc_fami = models.CharField(max_length=40, blank=True, null=True)
    desc_sist = models.CharField(max_length=60, blank=True, null=True)
    desc_equi = models.CharField(max_length=120, blank=True, null=True)
    desc_depa_emis_ifal = models.CharField(max_length=70, blank=True, null=True)
    desc_depa_ejec_ifal = models.CharField(max_length=50, blank=True, null=True)
    dias_tran_ulmo_ifal = models.IntegerField(blank=True, null=True)
    fech_ing_ifal = models.DateField(blank=True, null=True)
    mes_ing_ifal = models.CharField(max_length=25, blank=True, null=True)
    desc_esta_ifal = models.CharField(max_length=25, blank=True, null=True)
    fech_cier_ifal = models.DateField(blank=True, null=True)
    desc_falla_ifal = models.CharField(max_length=225, blank=True, null=True)
    desc_causa_ifal = models.CharField(max_length=275, blank=True, null=True)
    desc_solu_ifal = models.CharField(max_length=225, blank=True, null=True)
    tipo_falla = models.CharField(max_length=50, blank=True, null=True)
    esta_oper_unid = models.CharField(max_length=45, blank=True, null=True)
    esta_porc_unid = models.CharField(max_length=25, blank=True, null=True)
    esta_oper_sist = models.CharField(max_length=25, blank=True, null=True)
    esta_porc_sist = models.CharField(max_length=25, blank=True, null=True)
    esta_oper_equi = models.CharField(max_length=25, blank=True, null=True)
    esta_porc_equi = models.CharField(max_length=25, blank=True, null=True)
    nume_insp = models.CharField(max_length=25, blank=True, null=True)
    desc_falla_insp = models.CharField(max_length=225, blank=True, null=True)
    desc_causa_insp = models.CharField(max_length=225, blank=True, null=True)
    num_ortr = models.CharField(max_length=25, blank=True, null=True)
    desc_ortr = models.CharField(max_length=225, blank=True, null=True)
    componente = models.CharField(max_length=40, blank=True, null=True)
    fech_ingr_ortr = models.DateField(blank=True, null=True)
    mes_ingr_ortr = models.CharField(max_length=25, blank=True, null=True)
    desc_esta_ortr = models.CharField(max_length=25, blank=True, null=True)
    desc_depa_emis_ortr = models.CharField(max_length=200, blank=True, null=True)
    desc_depa_ejec_ortr = models.CharField(max_length=200, blank=True, null=True)
    fech_cierre_ortr = models.DateField(blank=True, null=True)
    depa_gene_reque = models.CharField(max_length=25, blank=True, null=True)
    nume_reque = models.CharField(max_length=25, blank=True, null=True)
    monto_reque = models.FloatField(blank=True, null=True)
    desc_esta_reque = models.CharField(max_length=25, blank=True, null=True)
    fech_regi_reque = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblTmpPrevent'
