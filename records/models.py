from django.db import models

# Create your models here.

class Client(models.Model):
    ClientID = models.CharField(unique = True)
    ClientName = models.CharField()
    CreatedOn = models.DateField()
    ShortName = models.CharField(unique = True)


class StagingRecords(models.Model):
	sr_no = models.IntegerField(unique = True)
	recruiter = models.ForeignKey('user.User')
	client = models.ForeignKey('Client')
	position = models.CharField()
	reqt_date = models.DateField()
	date_cv_submitted = models.DateField()
	candidate_name = models.CharField()
	current_status = models.IntegerField()
	current_status_desc = models.CharField()
	interview_date = models.DateField(blank = True)
	remarks = models.CharField(blank = True)
	skills = models.CharField()
	current_org = models.CharField()
	qualification = models.CharField()
	total_exp = models.FloatField()
	current_location = models.CharField()
	contact_details_mobile = models.IntegerField(max_len = 10)
	contact_details_phone2 = models.IntegerField(max_len = 10)
	email = models.EmailField()
    current_salary = models.DecimalField()
    expected_salary_percentage = models.IntegerField()
    expected_salary_amt = models.DecimalField()
    notice_period = models.DecimalField()
    Int_Tele_Date = models.DateField(blank = True)
    Int_Tele_Result = models.CharField(blank = True)
    Int_P1_Date = models.DateField(blank = True)
    Int_P1_Result = models.CharField(blank = True)
    Int_p2_Date = models.DateField(blank = True)
    Int_p2_Result = models.Charfield(blank = True)
    Int_p3_Date = models.DateField(blank = True)
    Int_p3_Result = models.Charfield(blank = True)
    Int_Final_Date = models.DateField(blank = True)
    Int_Final_Result = models.Charfield(blank = True)
    Int_HR_Date = models.DateField(blank = True)
    Int_HR_Result = models.Charfield(blank = True)
    offer_date = models.DateField(blank = True)
    offer_amt = models.DecimalField(blank = True)
    joining_date = models.DateField(blank = True)
    vacancy_code = models.Charfield(blank = True)
    applicant_code = models.Charfield(blank = True)
    DOB = models.DateField(blank = True)
    preferred_company = models.Charfield(blank = True)
    preferred_location = models.Charfield(blank = True)
    week_number = models.IntegerField(blank = True)
    wk_year = models.IntegerField(blank = True)

class GoodRecords(models.Model):
	sr_no = models.IntegerField(unique = True)
	recruiter = models.ForeignKey('user.User')
	client = models.ForeignKey('Client')
	position = models.CharField()
	reqt_date = models.DateField()
	date_cv_submitted = models.DateField()
	candidate_name = models.CharField()
	current_status = models.IntegerField()
	current_status_desc = models.CharField()
	interview_date = models.DateField(blank = True)
	remarks = models.CharField(blank = True)
	skills = models.CharField()
	current_org = models.CharField()
	qualification = models.CharField()
	total_exp = models.FloatField()
	current_location = models.CharField()
	contact_details_mobile = models.IntegerField(max_len = 10)
	contact_details_phone2 = models.IntegerField(max_len = 10)
	email = models.EmailField()
    current_salary = models.DecimalField()
    expected_salary_percentage = models.IntegerField()
    expected_salary_amt = models.DecimalField()
    notice_period = models.DecimalField()
    Int_Tele_Date = models.DateField(blank = True)
    Int_Tele_Result = models.CharField(blank = True)
    Int_P1_Date = models.DateField(blank = True)
    Int_P1_Result = models.CharField(blank = True)
    Int_p2_Date = models.DateField(blank = True)
    Int_p2_Result = models.Charfield(blank = True)
    Int_p3_Date = models.DateField(blank = True)
    Int_p3_Result = models.Charfield(blank = True)
    Int_Final_Date = models.DateField(blank = True)
    Int_Final_Result = models.Charfield(blank = True)
    Int_HR_Date = models.DateField(blank = True)
    Int_HR_Result = models.Charfield(blank = True)
    offer_date = models.DateField(blank = True)
    offer_amt = models.DecimalField(blank = True)
    joining_date = models.DateField(blank = True)
    vacancy_code = models.Charfield(blank = True)
    applicant_code = models.Charfield(blank = True)
    DOB = models.DateField(blank = True)
    preferred_company = models.Charfield(blank = True)
    preferred_location = models.Charfield(blank = True)
    week_number = models.IntegerField(blank = True)
    wk_year = models.IntegerField(blank = True)


class BadRecords(models.Model):
	sr_no = models.IntegerField(unique = True)
	recruiter = models.ForeignKey('user.User')
	client = models.ForeignKey('Client')
	position = models.CharField()
	reqt_date = models.DateField()
	date_cv_submitted = models.DateField()
	candidate_name = models.CharField()
	current_status = models.IntegerField()
	current_status_desc = models.CharField()
	interview_date = models.DateField(blank = True)
	remarks = models.CharField(blank = True)
	skills = models.CharField()
	current_org = models.CharField()
	qualification = models.CharField()
	total_exp = models.FloatField()
	current_location = models.CharField()
	contact_details_mobile = models.IntegerField(max_len = 10)
	contact_details_phone2 = models.IntegerField(max_len = 10)
	email = models.EmailField()
    current_salary = models.DecimalField()
    expected_salary_percentage = models.IntegerField()
    expected_salary_amt = models.DecimalField()
    notice_period = models.DecimalField()
    Int_Tele_Date = models.DateField(blank = True)
    Int_Tele_Result = models.CharField(blank = True)
    Int_P1_Date = models.DateField(blank = True)
    Int_P1_Result = models.CharField(blank = True)
    Int_p2_Date = models.DateField(blank = True)
    Int_p2_Result = models.Charfield(blank = True)
    Int_p3_Date = models.DateField(blank = True)
    Int_p3_Result = models.Charfield(blank = True)
    Int_Final_Date = models.DateField(blank = True)
    Int_Final_Result = models.Charfield(blank = True)
    Int_HR_Date = models.DateField(blank = True)
    Int_HR_Result = models.Charfield(blank = True)
    offer_date = models.DateField(blank = True)
    offer_amt = models.DecimalField(blank = True)
    joining_date = models.DateField(blank = True)
    vacancy_code = models.Charfield(blank = True)
    applicant_code = models.Charfield(blank = True)
    DOB = models.DateField(blank = True)
    preferred_company = models.Charfield(blank = True)
    preferred_location = models.Charfield(blank = True)
    week_number = models.IntegerField(blank = True)
    wk_year = models.IntegerField(blank = True)
    reason = models.Charfield(blank = True)
