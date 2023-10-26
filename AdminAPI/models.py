from django.db import models

## Create your models here.
#class Local(models.Model):
#	localid = models.AutoField(db_column="LocalId", primary_key=True) # Variável colocada com lowercase
#	localdescricao = models.CharField(db_column="LocalDescricao", max_length=100, db_collation="SQL_Latin1_General_CP1_CI_AS")
#	isactive = models.BooleanField(db_column="LocalIsActive") # Variável colocada com lowercase
#	creationuserid = models.IntegerField(db_column="CreationUserId") # Variável colocada com lowercase
#	creationdate = models.DateTimeField(db_column="CreationDate") # Variável colocada com lowercase
#	modificationuserid = models.IntegerField(db_column="ModificationUserId") # Variável colocada com lowercase
#	modificationdate = models.DateTimeField(db_column="ModificationDate") # Variável colocada com lowercase

	#class Meta:
	#	managed = False
	#	db_table = "Local"

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    alunoid = models.AutoField(db_column='AlunoId', primary_key=True)  # Field name made lowercase.
    alunonome = models.CharField(db_column='AlunoNome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunodatanascimento = models.DateTimeField(db_column='AlunoDataNascimento', blank=True, null=True)  # Field name made lowercase.
    alunonif = models.CharField(db_column='AlunoNif', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunocc = models.CharField(db_column='AlunoCC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunosegurancasocial = models.CharField(db_column='AlunosegurancaSocial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunonumeroutente = models.CharField(db_column='AlunoNumeroUtente', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunonacionalidade = models.CharField(db_column='AlunoNacionalidade', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunomorada = models.CharField(db_column='AlunoMorada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alunomoradacompleta = models.CharField(db_column='AlunoMoradaCompleta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paisid = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaisId', blank=True, null=True)  # Field name made lowercase.
    distritoid = models.ForeignKey('Distrito', models.DO_NOTHING, db_column='DistritoId', blank=True, null=True)  # Field name made lowercase.
    codigopostalid = models.ForeignKey('Codigopostal', models.DO_NOTHING, db_column='CodigoPostalId', blank=True, null=True)  # Field name made lowercase.
    concelhoid = models.ForeignKey('Concelho', models.DO_NOTHING, db_column='ConcelhoId', blank=True, null=True)  # Field name made lowercase.
    alunofoto = models.TextField(db_column='AlunoFoto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaoid = models.ForeignKey('Encarregadoeducacao', models.DO_NOTHING, db_column='EncarregadoEducacaoId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno'


class Alunoanoescolaridade(models.Model):
    alunoanoescolaridadeid = models.AutoField(db_column='AlunoAnoEscolaridadeId', primary_key=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId')  # Field name made lowercase.
    anoescolaridadeid = models.ForeignKey('Anoescolaridade', models.DO_NOTHING, db_column='AnoEscolaridadeId', blank=True, null=True)  # Field name made lowercase.
    anoletivoid = models.ForeignKey('Anoletivo', models.DO_NOTHING, db_column='AnoLetivoId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alunoanoescolaridade'


class Alunolocal(models.Model):
    alunolocalid = models.AutoField(db_column='AlunoLocalId', primary_key=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alunolocal'


class Anoescolaridade(models.Model):
    anoescolaridadeid = models.AutoField(db_column='AnoEscolaridadeId', primary_key=True)  # Field name made lowercase.
    anoescolaridadedescricao = models.CharField(db_column='AnoEscolaridadeDescricao', max_length=100)  # Field name made lowercase.
    anoescolaridadeisactive = models.IntegerField(db_column='AnoEscolaridadeIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anoescolaridade'


class Anoletivo(models.Model):
    anoletivoid = models.AutoField(db_column='AnoLetivoId', primary_key=True)  # Field name made lowercase.
    anoletivodescricao = models.CharField(db_column='AnoLetivoDescricao', max_length=100)  # Field name made lowercase.
    anoletivoisactive = models.IntegerField(db_column='AnoLetivoIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anoletivo'


class Atividade(models.Model):
    atividadeid = models.AutoField(db_column='AtividadeId', primary_key=True)  # Field name made lowercase.
    atividadename = models.CharField(db_column='AtividadeName', max_length=100)  # Field name made lowercase.
    atividadedescricao = models.CharField(db_column='AtividadeDescricao', max_length=100)  # Field name made lowercase.
    atividadelocalid = models.ForeignKey('Local', models.DO_NOTHING, db_column='AtividadeLocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade'


class Atividadealuno(models.Model):
    atividadealunoid = models.AutoField(db_column='AtividadeAlunoId', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeId', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    confirmado = models.IntegerField(db_column='Confirmado', blank=True, null=True)  # Field name made lowercase.
    validado = models.IntegerField(db_column='Validado', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividadealuno'


class Atividadecolaborador(models.Model):
    atividadecolaboradorid = models.AutoField(db_column='AtividadeColaboradorId', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeId', blank=True, null=True)  # Field name made lowercase.
    professorid = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    colaboradorid = models.ForeignKey('Colaborador', models.DO_NOTHING, db_column='ColaboradorId', blank=True, null=True)  # Field name made lowercase.
    responsavel = models.IntegerField(db_column='Responsavel', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividadecolaborador'


class Atividadetimetable(models.Model):
    atividadetimetableid = models.AutoField(db_column='AtividadeTimeTableId', primary_key=True)  # Field name made lowercase.
    atividadeid = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='AtividadeId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafim = models.DateTimeField(db_column='HoraFim', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividadetimetable'


class Codigopostal(models.Model):
    codigopostalid = models.AutoField(db_column='CodigoPostalId', primary_key=True)  # Field name made lowercase.
    codigopostalnomelocalidade = models.CharField(db_column='CodigoPostalNomeLocalidade', max_length=100)  # Field name made lowercase.
    codigopostalcodigolocalidade = models.CharField(db_column='CodigoPostalCodigoLocalidade', max_length=100)  # Field name made lowercase.
    codigopostaldesignacao = models.CharField(db_column='CodigoPostalDesignacao', max_length=100)  # Field name made lowercase.
    codigopostalnum = models.CharField(db_column='CodigoPostalNum', max_length=100)  # Field name made lowercase.
    codigopostalextensao = models.CharField(db_column='CodigoPostalExtensao', max_length=100)  # Field name made lowercase.
    codigopostalisactive = models.IntegerField(db_column='CodigoPostalIsActive', blank=True, null=True)  # Field name made lowercase.
    concelhoid = models.ForeignKey('Concelho', models.DO_NOTHING, db_column='ConcelhoId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codigopostal'


class Colaborador(models.Model):
    colaboradorid = models.AutoField(db_column='ColaboradorId', primary_key=True)  # Field name made lowercase.
    colaboradornome = models.CharField(db_column='ColaboradorNome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradordatanascimento = models.DateTimeField(db_column='ColaboradorDataNascimento', blank=True, null=True)  # Field name made lowercase.
    colaboradornif = models.CharField(db_column='ColaboradorNif', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradorcc = models.CharField(db_column='ColaboradorCC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradorsegurancasocial = models.CharField(db_column='ColaboradorsegurancaSocial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradornumeroutente = models.CharField(db_column='ColaboradorNumeroUtente', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradornacionalidade = models.CharField(db_column='ColaboradorNacionalidade', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradormorada = models.CharField(db_column='ColaboradorMorada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colaboradormoradacompleta = models.CharField(db_column='ColaboradorMoradaCompleta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paisid = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaisId', blank=True, null=True)  # Field name made lowercase.
    distritoid = models.ForeignKey('Distrito', models.DO_NOTHING, db_column='DistritoId', blank=True, null=True)  # Field name made lowercase.
    codigopostalid = models.ForeignKey(Codigopostal, models.DO_NOTHING, db_column='CodigoPostalId', blank=True, null=True)  # Field name made lowercase.
    concelhoid = models.ForeignKey('Concelho', models.DO_NOTHING, db_column='ConcelhoId', blank=True, null=True)  # Field name made lowercase.
    colaboradorfoto = models.TextField(db_column='ColaboradorFoto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaborador'


class Colaboradorlocal(models.Model):
    colaboradorlocalid = models.AutoField(db_column='ColaboradorLocalId', primary_key=True)  # Field name made lowercase.
    colaboradorid = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='ColaboradorId', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaboradorlocal'


class Concelho(models.Model):
    concelhoid = models.AutoField(db_column='ConcelhoId', primary_key=True)  # Field name made lowercase.
    concelhonome = models.CharField(db_column='ConcelhoNome', max_length=100)  # Field name made lowercase.
    concelhocodigo = models.CharField(db_column='ConcelhoCodigo', max_length=100)  # Field name made lowercase.
    concelhoisactive = models.IntegerField(db_column='ConcelhoIsActive', blank=True, null=True)  # Field name made lowercase.
    distritoid = models.ForeignKey('Distrito', models.DO_NOTHING, db_column='DistritoId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'concelho'


class Dia(models.Model):
    diaid = models.AutoField(db_column='DiaId', primary_key=True)  # Field name made lowercase.
    diadescricao = models.CharField(db_column='DiaDescricao', max_length=100)  # Field name made lowercase.
    diaisactive = models.IntegerField(db_column='DiaIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dia'


class Disciplina(models.Model):
    disciplinaid = models.AutoField(db_column='DisciplinaId', primary_key=True)  # Field name made lowercase.
    disciplinadescricao = models.CharField(db_column='DisciplinaDescricao', max_length=100)  # Field name made lowercase.
    disciplinaisactive = models.IntegerField(db_column='DisciplinaIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplina'


class Disciplinaexterna(models.Model):
    disciplinaexternaid = models.AutoField(db_column='DisciplinaExternaId', primary_key=True)  # Field name made lowercase.
    disciplinaexternadescricao = models.CharField(db_column='DisciplinaExternaDescricao', max_length=100)  # Field name made lowercase.
    disciplinaexternaisactive = models.IntegerField(db_column='DisciplinaExternaIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplinaexterna'


class Disciplinaexternaanoescolaridade(models.Model):
    disciplinaexternaanoescolaridadeid = models.AutoField(db_column='DisciplinaExternaAnoEscolaridadeId', primary_key=True)  # Field name made lowercase.
    disciplinaexternaid = models.ForeignKey(Disciplinaexterna, models.DO_NOTHING, db_column='DisciplinaExternaId')  # Field name made lowercase.
    anoescolaridadeid = models.ForeignKey(Anoescolaridade, models.DO_NOTHING, db_column='AnoEscolaridadeId', blank=True, null=True)  # Field name made lowercase.
    escalaid = models.ForeignKey('Escala', models.DO_NOTHING, db_column='EscalaId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplinaexternaanoescolaridade'


class Distrito(models.Model):
    distritoid = models.AutoField(db_column='DistritoId', primary_key=True)  # Field name made lowercase.
    distritonome = models.CharField(db_column='DistritoNome', max_length=100)  # Field name made lowercase.
    distritocodigo = models.CharField(db_column='DistritoCodigo', max_length=100)  # Field name made lowercase.
    distritoisactive = models.IntegerField(db_column='DistritoIsActive', blank=True, null=True)  # Field name made lowercase.
    paisid = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaisId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distrito'


class Ementa(models.Model):
    ementaid = models.AutoField(db_column='EmentaId', primary_key=True)  # Field name made lowercase.
    ementadescricao = models.CharField(db_column='EmentaDescricao', max_length=100)  # Field name made lowercase.
    ementafilename = models.CharField(db_column='EmentaFileName', max_length=100)  # Field name made lowercase.
    ementaext = models.CharField(db_column='EmentaExt', max_length=100)  # Field name made lowercase.
    ementaisactive = models.IntegerField(db_column='EmentaIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    ementabegindate = models.DateTimeField(db_column='EmentaBeginDate', blank=True, null=True)  # Field name made lowercase.
    ementaenddate = models.DateTimeField(db_column='EmentaEndDate', blank=True, null=True)  # Field name made lowercase.
    ementafile = models.TextField(db_column='EmentaFile', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ementa'


class Encarregadoeducacao(models.Model):
    encarregadoeducacaoid = models.AutoField(db_column='EncarregadoEducacaoId', primary_key=True)  # Field name made lowercase.
    encarregadoeducacaonome = models.CharField(db_column='EncarregadoEducacaoNome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaodatanascimento = models.DateTimeField(db_column='EncarregadoEducacaoDataNascimento', blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaonif = models.CharField(db_column='EncarregadoEducacaoNif', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaocc = models.CharField(db_column='EncarregadoEducacaoCC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaosegurancasocial = models.CharField(db_column='EncarregadoEducacaosegurancaSocial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaonumeroutente = models.CharField(db_column='EncarregadoEducacaoNumeroUtente', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaonacionalidade = models.CharField(db_column='EncarregadoEducacaoNacionalidade', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaomorada = models.CharField(db_column='EncarregadoEducacaoMorada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaomoradacompleta = models.CharField(db_column='EncarregadoEducacaoMoradaCompleta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paisid = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaisId', blank=True, null=True)  # Field name made lowercase.
    distritoid = models.ForeignKey(Distrito, models.DO_NOTHING, db_column='DistritoId', blank=True, null=True)  # Field name made lowercase.
    codigopostalid = models.ForeignKey(Codigopostal, models.DO_NOTHING, db_column='CodigoPostalId', blank=True, null=True)  # Field name made lowercase.
    concelhoid = models.ForeignKey(Concelho, models.DO_NOTHING, db_column='ConcelhoId', blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaofoto = models.TextField(db_column='EncarregadoEducacaoFoto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'encarregadoeducacao'


class Encarregadoeducacaolocal(models.Model):
    encarregadoeducacaolocalid = models.AutoField(db_column='EncarregadoEducacaoLocalId', primary_key=True)  # Field name made lowercase.
    encarregadoeducacaoid = models.ForeignKey(Encarregadoeducacao, models.DO_NOTHING, db_column='EncarregadoEducacaoId', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('Local', models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'encarregadoeducacaolocal'


class Equipa(models.Model):
    equipaid = models.AutoField(db_column='EquipaId', primary_key=True)  # Field name made lowercase.
    equipadescricao = models.CharField(db_column='EquipaDescricao', max_length=100)  # Field name made lowercase.
    equipaisactive = models.IntegerField(db_column='EquipaIsActive', blank=True, null=True)  # Field name made lowercase.
    equipalocalid = models.ForeignKey('Local', models.DO_NOTHING, db_column='EquipaLocalId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipa'


class Equipaelemento(models.Model):
    equipaelementoid = models.AutoField(db_column='EquipaElementoId', primary_key=True)  # Field name made lowercase.
    equipaid = models.ForeignKey(Equipa, models.DO_NOTHING, db_column='EquipaId', blank=True, null=True)  # Field name made lowercase.
    professorid = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    colaboradorid = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='ColaboradorId', blank=True, null=True)  # Field name made lowercase.
    responsavel = models.IntegerField(db_column='Responsavel', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipaelemento'


class Escala(models.Model):
    escalaid = models.AutoField(db_column='EscalaId', primary_key=True)  # Field name made lowercase.
    escaladescricao = models.CharField(db_column='EscalaDescricao', max_length=100)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'escala'


class Faltaaluno(models.Model):
    faltaalunoid = models.AutoField(db_column='FaltaAlunoId', primary_key=True)  # Field name made lowercase.
    turmadisciplinaid = models.ForeignKey('Turmadisciplina', models.DO_NOTHING, db_column='TurmaDisciplinaId', blank=True, null=True)  # Field name made lowercase.
    turmaservicoid = models.ForeignKey('Turmaservico', models.DO_NOTHING, db_column='TurmaServicoId', blank=True, null=True)  # Field name made lowercase.
    faltaalunojustificacao = models.CharField(db_column='FaltaAlunoJustificacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    justificada = models.IntegerField(db_column='Justificada', blank=True, null=True)  # Field name made lowercase.
    faltaalunojustificadaporuserid = models.IntegerField(db_column='FaltaAlunoJustificadaPorUserId', blank=True, null=True)  # Field name made lowercase.
    faltaalunodatajustificacao = models.DateTimeField(db_column='FaltaAlunoDataJustificacao', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faltaaluno'


class Globalsettings(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    setting = models.CharField(db_column='Setting', max_length=100)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'globalsettings'


class Grupo(models.Model):
    grupoid = models.AutoField(db_column='GrupoId', primary_key=True)  # Field name made lowercase.
    grupodescricao = models.CharField(db_column='GrupoDescricao', max_length=100)  # Field name made lowercase.
    grupoisactive = models.IntegerField(db_column='GrupoIsActive', blank=True, null=True)  # Field name made lowercase.
    perfilid = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='PerfilId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grupo'


class Local(models.Model):
    localid = models.AutoField(db_column='LocalId', primary_key=True)  # Field name made lowercase.
    localdescricao = models.CharField(db_column='LocalDescricao', max_length=100)  # Field name made lowercase.
    localisactive = models.IntegerField(db_column='LocalIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'local'


class Localsettings(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    setting = models.CharField(db_column='Setting', max_length=100)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localsettings'


class Nivel(models.Model):
    nivelid = models.AutoField(db_column='NivelId', primary_key=True)  # Field name made lowercase.
    niveldescricao = models.CharField(db_column='NivelDescricao', max_length=100)  # Field name made lowercase.
    escalaid = models.ForeignKey(Escala, models.DO_NOTHING, db_column='EscalaId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nivel'


class Notadisciplinaexternaaluno(models.Model):
    notadisciplinaexternaalunoid = models.AutoField(db_column='NotaDisciplinaExternaAlunoId', primary_key=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId')  # Field name made lowercase.
    disciplinaexternaanoescolaridadeid = models.ForeignKey(Disciplinaexternaanoescolaridade, models.DO_NOTHING, db_column='DisciplinaExternaAnoEscolaridadeId', blank=True, null=True)  # Field name made lowercase.
    periodoid = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='PeriodoId', blank=True, null=True)  # Field name made lowercase.
    nivelid = models.ForeignKey(Nivel, models.DO_NOTHING, db_column='NivelId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notadisciplinaexternaaluno'


class Notaturmadisciplina(models.Model):
    notaturmadisciplinaid = models.AutoField(db_column='NotaTurmaDisciplinaId', primary_key=True)  # Field name made lowercase.
    turmadisciplinaid = models.ForeignKey('Turmadisciplina', models.DO_NOTHING, db_column='TurmaDisciplinaId')  # Field name made lowercase.
    periodoid = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='PeriodoId')  # Field name made lowercase.
    observacoes = models.IntegerField(db_column='Observacoes', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notaturmadisciplina'


class Notaturmaservico(models.Model):
    notaturmaservicoid = models.AutoField(db_column='NotaTurmaServicoId', primary_key=True)  # Field name made lowercase.
    turmaservicoid = models.ForeignKey('Turmaservico', models.DO_NOTHING, db_column='TurmaServicoId')  # Field name made lowercase.
    periodoid = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='PeriodoId')  # Field name made lowercase.
    observacoes = models.IntegerField(db_column='Observacoes', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notaturmaservico'


class Notificacao(models.Model):
    notificacaoid = models.AutoField(db_column='NotificacaoId', primary_key=True)  # Field name made lowercase.
    notificacaoheader = models.CharField(db_column='NotificacaoHeader', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notificacaobody = models.CharField(db_column='NotificacaoBody', max_length=100)  # Field name made lowercase.
    notificacaofooter = models.CharField(db_column='NotificacaoFooter', max_length=100)  # Field name made lowercase.
    notificacaoisactive = models.IntegerField(db_column='NotificacaoIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId')  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notificacao'


class Ocorrenciaaluno(models.Model):
    ocorrenciaalunoid = models.AutoField(db_column='OcorrenciaAlunoId', primary_key=True)  # Field name made lowercase.
    turmadisciplinaid = models.ForeignKey('Turmadisciplina', models.DO_NOTHING, db_column='TurmaDisciplinaId', blank=True, null=True)  # Field name made lowercase.
    turmaservicoid = models.ForeignKey('Turmaservico', models.DO_NOTHING, db_column='TurmaServicoId', blank=True, null=True)  # Field name made lowercase.
    ocorrenciaalunoassunto = models.CharField(db_column='OcorrenciaAlunoAssunto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ocorrenciaalunotexto = models.CharField(db_column='OcorrenciaAlunoTexto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ocorrenciaaluno'


class Pais(models.Model):
    paisid = models.AutoField(db_column='PaisId', primary_key=True)  # Field name made lowercase.
    paisnome = models.CharField(db_column='PaisNome', max_length=100)  # Field name made lowercase.
    paisisocode = models.CharField(db_column='PaisISOCode', max_length=100)  # Field name made lowercase.
    paisisactive = models.IntegerField(db_column='PaisIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais'


class Perfil(models.Model):
    perfilid = models.AutoField(db_column='PerfilId', primary_key=True)  # Field name made lowercase.
    perfildescricao = models.CharField(db_column='PerfilDescricao', max_length=100)  # Field name made lowercase.
    perfilisactive = models.IntegerField(db_column='PerfilIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfil'


class Periodo(models.Model):
    periodoid = models.AutoField(db_column='PeriodoId', primary_key=True)  # Field name made lowercase.
    periododesignacao = models.CharField(db_column='PeriodoDesignacao', max_length=100)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'periodo'


class Permissao(models.Model):
    permissaoid = models.AutoField(db_column='PermissaoId', primary_key=True)  # Field name made lowercase.
    permissaodescription = models.CharField(db_column='PermissaoDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    screenid = models.ForeignKey('Screen', models.DO_NOTHING, db_column='ScreenId', blank=True, null=True)  # Field name made lowercase.
    grupoid = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='GrupoId', blank=True, null=True)  # Field name made lowercase.
    read = models.IntegerField(db_column='Read', blank=True, null=True)  # Field name made lowercase.
    write = models.IntegerField(db_column='Write', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissao'


class Professor(models.Model):
    professorid = models.AutoField(db_column='ProfessorId', primary_key=True)  # Field name made lowercase.
    professornome = models.CharField(db_column='ProfessorNome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professordatanascimento = models.DateTimeField(db_column='ProfessorDataNascimento', blank=True, null=True)  # Field name made lowercase.
    professornif = models.CharField(db_column='ProfessorNif', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professorcc = models.CharField(db_column='ProfessorCC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professorsegurancasocial = models.CharField(db_column='ProfessorsegurancaSocial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professornumeroutente = models.CharField(db_column='ProfessorNumeroUtente', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professornacionalidade = models.CharField(db_column='ProfessorNacionalidade', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professormorada = models.CharField(db_column='ProfessorMorada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    professormoradacompleta = models.CharField(db_column='ProfessorMoradaCompleta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paisid = models.ForeignKey(Pais, models.DO_NOTHING, db_column='PaisId', blank=True, null=True)  # Field name made lowercase.
    distritoid = models.ForeignKey(Distrito, models.DO_NOTHING, db_column='DistritoId', blank=True, null=True)  # Field name made lowercase.
    codigopostalid = models.ForeignKey(Codigopostal, models.DO_NOTHING, db_column='CodigoPostalId', blank=True, null=True)  # Field name made lowercase.
    concelhoid = models.ForeignKey(Concelho, models.DO_NOTHING, db_column='ConcelhoId', blank=True, null=True)  # Field name made lowercase.
    professorfoto = models.TextField(db_column='ProfessorFoto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'


class Professorlocal(models.Model):
    professorlocalid = models.AutoField(db_column='ProfessorLocalId', primary_key=True)  # Field name made lowercase.
    professorid = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professorlocal'


class Recurso(models.Model):
    recursoid = models.AutoField(db_column='RecursoId', primary_key=True)  # Field name made lowercase.
    professorid = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    recursodescricao = models.CharField(db_column='RecursoDescricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recursofilename = models.CharField(db_column='RecursoFileName', max_length=100)  # Field name made lowercase.
    recursoext = models.CharField(db_column='RecursoExt', max_length=100)  # Field name made lowercase.
    recursoisactive = models.IntegerField(db_column='RecursoIsActive', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    tiporecursoid = models.ForeignKey('Tiporecurso', models.DO_NOTHING, db_column='TipoRecursoId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recurso'


class Refeicao(models.Model):
    refeicaoid = models.AutoField(db_column='RefeicaoId', primary_key=True)  # Field name made lowercase.
    refeicaodescricao = models.CharField(db_column='RefeicaoDescricao', max_length=100)  # Field name made lowercase.
    refeicaoisactive = models.IntegerField(db_column='RefeicaoIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'refeicao'


class Refeicaoaluno(models.Model):
    refeicaoalunoid = models.AutoField(db_column='RefeicaoAlunoId', primary_key=True)  # Field name made lowercase.
    refeicaoid = models.ForeignKey(Refeicao, models.DO_NOTHING, db_column='RefeicaoId', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'refeicaoaluno'


class Rota(models.Model):
    rotaid = models.AutoField(db_column='RotaId', primary_key=True)  # Field name made lowercase.
    rotadescricao = models.CharField(db_column='RotaDescricao', max_length=100)  # Field name made lowercase.
    rotaisactive = models.IntegerField(db_column='RotaIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rota'


class Rotaaluno(models.Model):
    rotaalunoid = models.AutoField(db_column='RotaAlunoId', primary_key=True)  # Field name made lowercase.
    rotaid = models.ForeignKey(Rota, models.DO_NOTHING, db_column='RotaId', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotaaluno'


class Rotano(models.Model):
    rotanoid = models.AutoField(db_column='RotaNoId', primary_key=True)  # Field name made lowercase.
    rotaid = models.ForeignKey(Rota, models.DO_NOTHING, db_column='RotaId', blank=True, null=True)  # Field name made lowercase.
    rotaposicao = models.IntegerField(db_column='RotaPosicao', blank=True, null=True)  # Field name made lowercase.
    rotalocal = models.CharField(db_column='RotaLocal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rotacoordenadas = models.CharField(db_column='RotaCoordenadas', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotano'


class Rotatimetable(models.Model):
    rotatimetableid = models.AutoField(db_column='RotaTimeTableId', primary_key=True)  # Field name made lowercase.
    rotaid = models.ForeignKey(Rota, models.DO_NOTHING, db_column='RotaId', blank=True, null=True)  # Field name made lowercase.
    colaboradorid = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='ColaboradorId', blank=True, null=True)  # Field name made lowercase.
    veiculoid = models.ForeignKey('Veiculo', models.DO_NOTHING, db_column='VeiculoId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafim = models.DateTimeField(db_column='HoraFim', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotatimetable'


class Sala(models.Model):
    salaid = models.AutoField(db_column='SalaId', primary_key=True)  # Field name made lowercase.
    saladescricao = models.CharField(db_column='SalaDescricao', max_length=100)  # Field name made lowercase.
    salaisactive = models.IntegerField(db_column='SalaIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sala'


class Screen(models.Model):
    screenid = models.AutoField(db_column='ScreenId', primary_key=True)  # Field name made lowercase.
    screenname = models.CharField(db_column='ScreenName', max_length=100)  # Field name made lowercase.
    screenisactive = models.IntegerField(db_column='ScreenIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'screen'


class Servico(models.Model):
    servicoid = models.AutoField(db_column='ServicoId', primary_key=True)  # Field name made lowercase.
    servicodescricao = models.CharField(db_column='ServicoDescricao', max_length=100)  # Field name made lowercase.
    servicoisactive = models.IntegerField(db_column='ServicoIsActive', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey(Local, models.DO_NOTHING, db_column='LocalId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servico'


class Systemlog(models.Model):
    systemlogid = models.AutoField(db_column='SystemLogId', primary_key=True)  # Field name made lowercase.
    systemlogtablename = models.CharField(db_column='SystemLogTableName', max_length=100)  # Field name made lowercase.
    systemlogdata = models.CharField(db_column='SystemLogData', max_length=100)  # Field name made lowercase.
    systemloglocalid = models.IntegerField(db_column='SystemLogLocalId', blank=True, null=True)  # Field name made lowercase.
    systemloguserid = models.IntegerField(db_column='SystemLogUserId', blank=True, null=True)  # Field name made lowercase.
    systemlogdate = models.DateTimeField(db_column='SystemLogDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'systemlog'


class Tarefa(models.Model):
    tarefaid = models.AutoField(db_column='TarefaId', primary_key=True)  # Field name made lowercase.
    turmadisciplinaid = models.ForeignKey('Turmadisciplina', models.DO_NOTHING, db_column='TurmaDisciplinaId', blank=True, null=True)  # Field name made lowercase.
    turmaservicoid = models.ForeignKey('Turmaservico', models.DO_NOTHING, db_column='TurmaServicoId', blank=True, null=True)  # Field name made lowercase.
    tarefaassunto = models.CharField(db_column='TarefaAssunto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tarefatexto = models.CharField(db_column='TarefaTexto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tarefadataentrega = models.DateTimeField(db_column='TarefaDataEntrega', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarefa'


class Tarefaaluno(models.Model):
    tarefaalunoid = models.AutoField(db_column='TarefaAlunoId', primary_key=True)  # Field name made lowercase.
    tarefaid = models.ForeignKey(Tarefa, models.DO_NOTHING, db_column='TarefaId', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    tarefaalunoentregue = models.IntegerField(db_column='TarefaAlunoEntregue', blank=True, null=True)  # Field name made lowercase.
    tarefaalunodataentrega = models.DateTimeField(db_column='TarefaAlunoDataEntrega', blank=True, null=True)  # Field name made lowercase.
    tarefaalunovalidada = models.IntegerField(db_column='TarefaAlunoValidada', blank=True, null=True)  # Field name made lowercase.
    tarefaalunodatavalidacao = models.DateTimeField(db_column='TarefaAlunoDataValidacao', blank=True, null=True)  # Field name made lowercase.
    tarefaalunotexto = models.CharField(db_column='TarefaAlunoTexto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarefaaluno'


class Tarefaalunoficheiro(models.Model):
    tarefaalunoficheiroid = models.AutoField(db_column='TarefaAlunoFicheiroId', primary_key=True)  # Field name made lowercase.
    tarefaalunoid = models.ForeignKey(Tarefaaluno, models.DO_NOTHING, db_column='TarefaAlunoId', blank=True, null=True)  # Field name made lowercase.
    tarefaalunoficheirofilename = models.CharField(db_column='TarefaAlunoFicheiroFileName', max_length=100)  # Field name made lowercase.
    tarefaalunoficheiroext = models.CharField(db_column='TarefaAlunoFicheiroExt', max_length=100)  # Field name made lowercase.
    tarefaalunoficheiroisactive = models.IntegerField(db_column='TarefaAlunoFicheiroIsActive', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarefaalunoficheiro'


class Tarefaficheiro(models.Model):
    tarefaficheiroid = models.AutoField(db_column='TarefaFicheiroId', primary_key=True)  # Field name made lowercase.
    tarefaid = models.ForeignKey(Tarefa, models.DO_NOTHING, db_column='TarefaId', blank=True, null=True)  # Field name made lowercase.
    tarefaficheirofilename = models.CharField(db_column='TarefaFicheiroFileName', max_length=100)  # Field name made lowercase.
    tarefaficheiroext = models.CharField(db_column='TarefaFicheiroExt', max_length=100)  # Field name made lowercase.
    tarefaficheiroisactive = models.IntegerField(db_column='TarefaFicheiroIsActive', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarefaficheiro'


class Tiporecurso(models.Model):
    tiporecursoid = models.AutoField(db_column='TipoRecursoId', primary_key=True)  # Field name made lowercase.
    tiporecursodescricao = models.CharField(db_column='TipoRecursoDescricao', max_length=100)  # Field name made lowercase.
    tiporecursoisactive = models.IntegerField(db_column='TipoRecursoIsActive', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiporecurso'


class Turma(models.Model):
    turmaid = models.AutoField(db_column='TurmaId', primary_key=True)  # Field name made lowercase.
    turmadesignacao = models.CharField(db_column='TurmaDesignacao', max_length=100)  # Field name made lowercase.
    turmaisactive = models.IntegerField(db_column='TurmaIsActive', blank=True, null=True)  # Field name made lowercase.
    turmalocalid = models.ForeignKey(Local, models.DO_NOTHING, db_column='TurmaLocalId')  # Field name made lowercase.
    turmaanoletivoid = models.ForeignKey(Anoletivo, models.DO_NOTHING, db_column='TurmaAnoLetivoId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turma'


class Turmaaluno(models.Model):
    turmaalunoid = models.AutoField(db_column='TurmaAlunoId', primary_key=True)  # Field name made lowercase.
    turmaid = models.ForeignKey(Turma, models.DO_NOTHING, db_column='TurmaId', blank=True, null=True)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmaaluno'


class Turmadisciplina(models.Model):
    turmadisciplinaid = models.AutoField(db_column='TurmaDisciplinaId', primary_key=True)  # Field name made lowercase.
    turmaid = models.ForeignKey(Turma, models.DO_NOTHING, db_column='TurmaId', blank=True, null=True)  # Field name made lowercase.
    disciplinaid = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='DisciplinaId', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmadisciplina'


class Turmadisciplinatimetable(models.Model):
    turmadisciplinatimetableid = models.AutoField(db_column='TurmaDisciplinaTimetableId', primary_key=True)  # Field name made lowercase.
    turmadisciplinaid = models.ForeignKey(Turmadisciplina, models.DO_NOTHING, db_column='TurmaDisciplinaId', blank=True, null=True)  # Field name made lowercase.
    diaid = models.ForeignKey(Dia, models.DO_NOTHING, db_column='DiaId', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafim = models.DateTimeField(db_column='HoraFim', blank=True, null=True)  # Field name made lowercase.
    datainicio = models.DateTimeField(db_column='DataInicio', blank=True, null=True)  # Field name made lowercase.
    datafim = models.DateTimeField(db_column='DataFim', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmadisciplinatimetable'


class Turmaservico(models.Model):
    turmaservicoid = models.AutoField(db_column='TurmaServicoId', primary_key=True)  # Field name made lowercase.
    turmaid = models.ForeignKey(Turma, models.DO_NOTHING, db_column='TurmaId', blank=True, null=True)  # Field name made lowercase.
    servicoid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='ServicoId', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmaservico'


class Turmaservicoresponsavel(models.Model):
    turmaservicoresponsavelid = models.AutoField(db_column='TurmaServicoResponsavelId', primary_key=True)  # Field name made lowercase.
    turmaservicoid = models.ForeignKey(Turmaservico, models.DO_NOTHING, db_column='TurmaServicoId', blank=True, null=True)  # Field name made lowercase.
    professorid = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    colaboradorid = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='ColaboradorId', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmaservicoresponsavel'


class Turmaservicotimetable(models.Model):
    turmaservicotimetableid = models.AutoField(db_column='TurmaServicoTimetableId', primary_key=True)  # Field name made lowercase.
    turmaservicoid = models.ForeignKey(Turmaservico, models.DO_NOTHING, db_column='TurmaServicoId', blank=True, null=True)  # Field name made lowercase.
    diaid = models.ForeignKey(Dia, models.DO_NOTHING, db_column='DiaId', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafim = models.DateTimeField(db_column='HoraFim', blank=True, null=True)  # Field name made lowercase.
    datainicio = models.DateTimeField(db_column='DataInicio', blank=True, null=True)  # Field name made lowercase.
    datafim = models.DateTimeField(db_column='DataFim', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turmaservicotimetable'


class Utilizador(models.Model):
    utilizadorid = models.AutoField(db_column='UtilizadorId', primary_key=True)  # Field name made lowercase.
    utilizadoremail = models.CharField(db_column='UtilizadorEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    utilizadoremailconfirmed = models.IntegerField(db_column='UtilizadorEmailConfirmed')  # Field name made lowercase.
    utilizadorisactive = models.IntegerField(db_column='UtilizadorIsActive')  # Field name made lowercase.
    utilizadorpasswordhash = models.CharField(db_column='UtilizadorPasswordHash', max_length=100)  # Field name made lowercase.
    utilizadoractivationkey = models.CharField(db_column='UtilizadorActivationKey', max_length=100)  # Field name made lowercase.
    alunoid = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='AlunoId', blank=True, null=True)  # Field name made lowercase.
    professorid = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    encarregadoeducacaoid = models.ForeignKey(Encarregadoeducacao, models.DO_NOTHING, db_column='EncarregadoEducacaoId', blank=True, null=True)  # Field name made lowercase.
    colaboradorid = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='ColaboradorId', blank=True, null=True)  # Field name made lowercase.
    utilizadorpassword = models.CharField(db_column='UtilizadorPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador'


class Utilizadorgrupo(models.Model):
    utilizadorgrupoid = models.AutoField(db_column='UtilizadorGrupoId', primary_key=True)  # Field name made lowercase.
    grupoid = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='GrupoId', blank=True, null=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey(Utilizador, models.DO_NOTHING, db_column='UtilizadorId', blank=True, null=True)  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizadorgrupo'


class Veiculo(models.Model):
    veiculoid = models.AutoField(db_column='VeiculoId', primary_key=True)  # Field name made lowercase.
    veiculomatricula = models.CharField(db_column='VeiculoMatricula', max_length=100)  # Field name made lowercase.
    localid = models.IntegerField(db_column='LocalId')  # Field name made lowercase.
    creationuserid = models.IntegerField(db_column='CreationUserId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.IntegerField(db_column='ModificationUserId', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'veiculo'
