from django.db import models
import uuid

class legal_forms(models.Model):
    legal_form = models.CharField(max_length=4)

class sectors(models.Model):
    name = models.CharField(max_length=100)    

class empl_statuses(models.Model):
    employment_status = models.CharField(max_length=100)   

class account_types(models.Model):
    type = models.CharField(max_length=50)    

class contact_methods(models.Model):
    method = models.CharField(max_length=50)     

class currencies(models.Model):
    ISO_code = models.CharField(max_length=3)    
    currency = models.CharField(max_length=50)
    symbol = models.CharField(max_length=1)

class est_investments(models.Model):
    amount = models.CharField(max_length=30)  

class genders(models.Model):
    gender = models.CharField(max_length=6)    

class marital_statuses(models.Model):
    status = models.CharField(max_length=9)    

class reception_methods(models.Model):
    method = models.CharField(max_length=30)

class salutations(models.Model):
    abbreviation = models.CharField(max_length=4)    
    full_version = models.CharField(max_length=8)

class total_assets(models.Model):
    amount = models.CharField(max_length=30)    

class about_company(models.Model):
    short_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    legal_form = models.ForeignKey(legal_forms, on_delete=models.CASCADE)

class annual_net_incomes(models.Model):
    amount = models.CharField(max_length=30)

class countries(models.Model):
    short_name = models.CharField(max_length=2)    
    full_name = models.CharField(max_length=30)

class corporate_forms(models.Model):
    code = models.CharField(max_length=4)    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    jurisdiction = models.ForeignKey(countries, on_delete=models.CASCADE)

class data_subscribers(models.Model):
    status = models.CharField(max_length=20)

class family_members(models.Model):
    relationship = models.CharField(max_length=20)    

class id_types(models.Model):
    name = models.CharField(max_length=20)    

class net_worths(models.Model):
    amount = models.CharField(max_length=30)    

class risk_tolerances(models.Model):
    tolerance = models.CharField(max_length=20)    

class tax_classifications(models.Model):
    name = models.CharField(max_length=30)    
    full_name = models.CharField(max_length=50)

class agents(models.Model):
    agent_name = models.CharField(max_length=50)    
    agent_commission = models.FloatField()
    notes = models.CharField(max_length=10)

class customers(models.Model):
    salutation = models.ForeignKey(salutations, on_delete=models.CASCADE)    
    gender = models.ForeignKey(genders, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    birth_country = models.ForeignKey(countries, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(marital_statuses, on_delete=models.CASCADE)
    dependant_number = models.FloatField()
    id_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class accounts(models.Model):
    account_no = models.CharField(max_length=34)
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    base_currency = models.ForeignKey(currencies, on_delete=models.CASCADE)
    account_type = models.ForeignKey(account_types, on_delete=models.CASCADE)
    agreement_no = models.CharField(max_length=30)
    agreement_date = models.DateField()
    management_fee = models.DecimalField(max_digits=100, decimal_places=2)
    company_reg_num = models.CharField(max_length=30)

class custodians(models.Model):
    short_name = models.CharField(max_length=30)    
    full_name = models.CharField(max_length=50)
    special_mark = models.CharField(max_length=10)
    iban = models.CharField(max_length=34)
    custodian_documents = models.FileField(upload_to='documents/')
    account_number = models.ForeignKey(accounts, on_delete=models.CASCADE)

class counterparties(models.Model):
    short_name = models.CharField(max_length=3)   
    full_name = models.CharField(max_length=30)
    bic = models.CharField(max_length=10)
    mifis_status = models.CharField(max_length=10)
    resident_country = models.ForeignKey(countries, on_delete=models.CASCADE)
    counterparty_documents = models.FileField(upload_to='documents/')

class mifid_types(models.Model):
    type = models.CharField(max_length=20)    

class branches(models.Model):
    location = models.CharField(max_length=30)    

class stock_exchanges(models.Model):
    short_name = models.CharField(max_length=40)    
    name = models.CharField(max_length=100) 
    mic = models.CharField(max_length=20) 
    in_eea = models.BooleanField()
    city = models.CharField(max_length=50)
    country = models.ForeignKey(countries, on_delete=models.CASCADE)

class issuers(models.Model):
    name = models.CharField(max_length=50) 
    sector = models.ForeignKey(sectors, on_delete=models.CASCADE)    
    country = models.ForeignKey(countries, on_delete=models.CASCADE)

class counterparty_custodians(models.Model):
    custodian = models.ForeignKey(custodians, on_delete=models.CASCADE)    
    counterparty = models.ForeignKey(counterparties, on_delete=models.CASCADE)

class instrument_types(models.Model):
    type = models.CharField(max_length=10)    

class instruments(models.Model):
    currency = models.ForeignKey(currencies, on_delete=models.CASCADE)    
    type = models.ForeignKey(instrument_types, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    issuer = models.ForeignKey(issuers, on_delete=models.CASCADE)
    country = models.ForeignKey(countries, on_delete=models.CASCADE)
    isin = models.CharField(max_length=20)
    start_date = models.DateField()
    maturity_date = models.DateField()
    coupon_rate = models.FloatField()

class instrument_risks(models.Model):
    rating = models.FloatField(default=0)   
    description = models.TextField()

class prices(models.Model):
    instrument = models.ForeignKey(instruments, on_delete=models.CASCADE)     
    date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

class durations(models.Model):
    term = models.CharField(max_length=10)    
    good = models.BooleanField()

class instrument_rates(models.Model):
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    mifid_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE)
    r1_allowed = models.BooleanField()
    r2_allowed = models.BooleanField()
    r3_allowed = models.BooleanField()
    r4_allowed = models.BooleanField()
    r5_allowed = models.BooleanField()
    r6_allowed = models.BooleanField()
    r7_allowed = models.BooleanField()
    r8_allowed = models.BooleanField()
    r1_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r1_type')
    r2_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r2_type')
    r3_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r3_type')
    r4_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r4_type')
    r5_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r5_type')
    r6_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r6_type')
    r7_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r7_type')
    r8_type = models.ForeignKey(mifid_types, on_delete=models.CASCADE, related_name='r8_type')

class id_documents(models.Model):
    id_document = models.CharField(max_length=30)    
    issue_date = models.DateField()
    document_no = models.CharField(max_length=30)
    expire_date = models.DateField()
    customer_no = models.ForeignKey(customers, on_delete=models.CASCADE)
    citizenship = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='citizenship')
    residence = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='residence')
    issuing_authority = models.CharField(max_length=30)

class customer_education(models.Model):
    high_school = models.BooleanField()
    undergraduate = models.BooleanField()
    graduate = models.BooleanField()
    customer_no = models.ForeignKey(customers, on_delete=models.CASCADE)    

class customer_consent(models.Model):
    submit_orders = models.ForeignKey(contact_methods, on_delete=models.CASCADE, related_name='cc_submit_orders')    
    submit_documents = models.ForeignKey(contact_methods, on_delete=models.CASCADE, related_name='submit_documents')
    customer_no = models.ForeignKey(customers, on_delete=models.CASCADE)

class fatca(models.Model):
    tax_resi_coun = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='tax_resi_coun')    
    tax_payer_id = models.CharField(max_length=30)
    auth_sign_pres = models.BooleanField()
    salutation = models.ForeignKey(salutations, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    home_phone = models.CharField(max_length=30)
    mobile_phone = models.CharField(max_length=30)
    email = models.EmailField()
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=50)
    act_base_on_docu = models.CharField(max_length=50)
    document_date = models.DateField()
    document_no = models.CharField(max_length=30)
    country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='f_country')
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    id_document = models.FileField(upload_to='documents/')
    personal_id = models.CharField(max_length=30)
    id_issue_date = models.DateField()
    id_expire_date = models.DateField()
    issuing_authority = models.CharField(max_length=50)
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class kyc(models.Model):
    net_worth = models.ForeignKey(net_worths, on_delete=models.CASCADE, related_name='kyc_net_worth')    
    liquid_worth = models.ForeignKey(net_worths, on_delete=models.CASCADE, related_name='kyc_liquid_worth')
    annual_net_income = models.ForeignKey(annual_net_incomes, on_delete=models.CASCADE)
    total_asset = models.ForeignKey(net_worths, on_delete=models.CASCADE, related_name='kyc_total_asset')
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class regulatory_info(models.Model):
    client_related_finance = models.BooleanField()
    fam_mem_rel_fin_ser = models.BooleanField()
    fam_mem_name_from_fin_ser = models.CharField(max_length=50)
    fam_mem_rel_from_fin_ser = models.ForeignKey(family_members, on_delete=models.CASCADE, related_name='ri_fam_mem_rel_from_fin_ser')
    fin_ser_com_name = models.CharField(max_length=50)
    pos_in_fin_ser_com = models.CharField(max_length=50)
    fin_ser_com_cou = models.ForeignKey(countries, on_delete=models.CASCADE)
    fsc_state = models.CharField(max_length=30)
    fsc_city = models.CharField(max_length=30)
    fsc_zipcode = models.CharField(max_length=20)
    fsc_address = models.CharField(max_length=200)
    fsc_phone1 = models.CharField(max_length=30)
    fsc_phone2 = models.CharField(max_length=30)
    cli_rel_to_mar_reg = models.BooleanField()
    cli_fam_mem_rel_to_mar_reg = models.BooleanField()
    fam_mem_name_from_mar_reg = models.CharField(max_length=50)
    fam_mem_rel_from_mar_reg = models.ForeignKey(family_members, on_delete=models.CASCADE, related_name='ri_fam_mem_rel_from_mar_reg')
    pos_in_mar_reg = models.CharField(max_length=50)
    cli_pub_com_con_per = models.BooleanField()
    public_company_name = models.CharField(max_length=50)
    unresolved_financial_disputes = models.BooleanField()
    unr_fin_dis_desc = models.TextField()
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class customer_contacts(models.Model):
    country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='cc_country')
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    mobile1 = models.CharField(max_length=30)
    con_me_on_mob1 = models.BooleanField()
    mobile2 = models.CharField(max_length=30)
    email = models.EmailField()
    con_me_on_email = models.BooleanField()
    mail_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='mail_country')
    mail_state = models.CharField(max_length=50)
    mail_city = models.CharField(max_length=50)
    mail_zipcode = models.CharField(max_length=20)
    mail_address = models.CharField(max_length=200)
    tax_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='tax_country')
    tax_id_no = models.CharField(max_length=30)
    add_tax_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='add_tax_country')
    add_tax_id_no = models.CharField(max_length=30)
    grandmother_firstname = models.CharField(max_length=50)
    father_profession = models.CharField(max_length=50)
    first_pet_name = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    swift = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class customer_empl(models.Model):
    employ_status = models.ForeignKey(empl_statuses, on_delete=models.CASCADE)
    empl_name = models.CharField(max_length=50)
    business_nature = models.CharField(max_length=50)
    sector = models.ForeignKey(sectors, on_delete=models.CASCADE)
    empl_country = models.ForeignKey(countries, on_delete=models.CASCADE)
    emp_state = models.CharField(max_length=50)
    empl_city = models.CharField(max_length=50)
    empl_zipcode = models.CharField(max_length=20)
    empl_address = models.CharField(max_length=200)
    empl_phone = models.CharField(max_length=30)
    job_title = models.CharField(max_length=50)
    current_position_months = models.CharField(max_length=50)
    work_experience_months = models.CharField(max_length=50)
    consulting_income = models.FloatField()
    interest_income = models.FloatField()
    real_estate_income = models.FloatField()
    rental_income = models.FloatField()
    trading_income = models.FloatField()
    inheritance_income = models.FloatField()
    spouse_income = models.FloatField()
    severance_income = models.FloatField()
    unemployment_aid = models.FloatField()
    disability_aid = models.FloatField()
    retirement = models.FloatField()
    other_income = models.FloatField()
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class sanctions(models.Model):
    cli_con_with_iran_govt_or_ofac_un_eu_list_enti = models.BooleanField()
    con_with_iran_govt_or_ofac_un_eu_list_enti = models.CharField(max_length=50)
    client_acting_for = models.BooleanField()
    activity_desc = models.TextField()
    cli_act_in_ofac_san_sec = models.BooleanField()
    sanctioned_sector = models.ForeignKey(sectors, on_delete=models.CASCADE)
    dir_or_ind_bus_with_iran_govt_or_ofac_un_eu_list_enti = models.BooleanField()
    business_activity_details = models.TextField()
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class investment_obj(models.Model):
    hedging = models.BooleanField()
    income = models.BooleanField()
    growth = models.BooleanField()
    trading_profits = models.BooleanField()
    speculation = models.BooleanField()
    capital_preservation = models.BooleanField()
    currency = models.ForeignKey(currencies, on_delete=models.CASCADE)
    usa = models.BooleanField()
    australia = models.BooleanField()
    austria = models.BooleanField()
    belgium = models.BooleanField()
    canada = models.BooleanField()
    czech_rep = models.BooleanField()
    italy = models.BooleanField()
    singapore = models.BooleanField()
    georgia = models.BooleanField()
    denmark = models.BooleanField()
    france = models.BooleanField()
    germany = models.BooleanField()
    hong_kong = models.BooleanField()
    india = models.BooleanField()
    japan = models.BooleanField()
    mexico = models.BooleanField()
    netherlands = models.BooleanField()
    norway = models.BooleanField()
    portugal = models.BooleanField()
    south_korea = models.BooleanField()
    spain = models.BooleanField()
    sweden = models.BooleanField()
    switzerland = models.BooleanField()
    uk = models.BooleanField()
    eu = models.BooleanField()
    international = models.BooleanField()
    international_except_georgia = models.BooleanField()
    stocks = models.BooleanField()
    warrants = models.BooleanField()
    etf = models.BooleanField()
    mutual_fund = models.BooleanField()
    bonds = models.BooleanField()
    cfd = models.BooleanField()
    metals = models.BooleanField()
    options = models.BooleanField()
    futures = models.BooleanField()
    spreads = models.BooleanField()
    investment_amount = models.ForeignKey(est_investments, on_delete=models.CASCADE)
    risk_tolerance = models.ForeignKey(risk_tolerances, on_delete=models.CASCADE)
    scalper = models.BooleanField()
    swinger = models.BooleanField()
    short_term_investor = models.BooleanField()
    low_int_term_inv = models.BooleanField()
    high_int_term_inv = models.BooleanField()
    long_term_investor = models.BooleanField()
    data_subs_status = models.ForeignKey(data_subscribers, on_delete=models.CASCADE)
    cli_will_not_subs_sta_cng = models.BooleanField()
    cli_agr_to_per_use_only = models.BooleanField()
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    com_reg_num = models.CharField(max_length=50)

class political_exposure(models.Model):
    senior_public_position = models.BooleanField()
    legislature = models.BooleanField()
    high_court_member = models.BooleanField()
    high_ranked_military = models.BooleanField()
    cen_bank_cou_mem = models.BooleanField()
    ambassador = models.BooleanField()
    sta_own_ent_brd_mem = models.BooleanField()
    pol_par_sen_exe = models.BooleanField()
    pol_prt_name = models.CharField(max_length=50)
    imm_fml_mem_pol_exp = models.BooleanField()
    pol_exp_fml_mem_rel = models.ForeignKey(family_members, on_delete=models.CASCADE)
    pol_prt_snr_exe_ast_hld = models.BooleanField()
    gvt_snr_exe_ass_hld = models.BooleanField()
    plt_exp_fam_mbr_name = models.CharField(max_length=50)
    ccg = models.BooleanField()
    real_account_beneficiary = models.CharField(max_length=50)
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)

class company_types(models.Model):
    type  = models.CharField(max_length=50)    

class companies(models.Model):
    legal_form = models.ForeignKey(legal_forms, on_delete=models.CASCADE)    
    entity_name = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=30)
    reg_date = models.DateField()
    reg_edit_date = models.DateField()
    activity_countries = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='activity_countries')
    incorporation_countries = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='incorporation_countries')
    contact_name = models.CharField(max_length=50)
    phone = models.BooleanField()
    email = models.EmailField()
    website = models.CharField(max_length=50)
    lega_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='lega_country')
    lega_state = models.CharField(max_length=50)
    lega_city = models.CharField(max_length=50)
    lega_zipcode = models.CharField(max_length=20)
    lega_address = models.CharField(max_length=200)
    maa_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='maa_country')
    maa_state = models.CharField(max_length=50)
    maa_city = models.CharField(max_length=50)
    maa_zipcode = models.CharField(max_length=20)
    maa_address = models.CharField(max_length=200)    
    is_operating_business = models.BooleanField()
    business_desc = models.TextField()
    investment_company_type = models.ForeignKey(company_types, on_delete=models.CASCADE)
    is_rel_to_crt = models.BooleanField()
    annual_turnover = models.ForeignKey(annual_net_incomes, on_delete=models.CASCADE, related_name='annual_turnover')
    net_annual_income = models.ForeignKey(annual_net_incomes, on_delete=models.CASCADE, related_name='net_annual_income')
    estimated_net_worth  = models.ForeignKey(net_worths, on_delete=models.CASCADE)
    total_assets = models.ForeignKey(total_assets, on_delete=models.CASCADE)
    acc_opening_purpose = models.CharField(max_length=50)
    fund_source = models.CharField(max_length=50)
    tax_residency = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='c_tax_residency')
    govt_id_no = models.CharField(max_length=30)
    second_tax_residency = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='second_tax_residency')
    tax_id_no = models.CharField(max_length=30)

class company_documents(models.Model):
    eee = models.FloatField()

class us_tax_classifications(models.Model):
    classification = models.CharField(max_length=50)  

class company_regulations(models.Model):
    foreign_bank = models.BooleanField()    
    security_broker = models.BooleanField() 
    futures_commission_merchant = models.BooleanField() 
    introducing = models.BooleanField() 
    non_us_brn_of_sec_mtl_fund = models.BooleanField() 
    mutual_fund = models.BooleanField() 
    employee_benefit_plan = models.BooleanField() 
    money_transmitter = models.BooleanField() 
    excahnger = models.BooleanField() 
    trader = models.BooleanField() 
    retail_fx_dealer = models.BooleanField() 
    life_insurance_company = models.BooleanField() 
    us_bank = models.BooleanField() 
    sec_reg_inv_com = models.BooleanField() 
    excahnge_traded_company = models.BooleanField() 
    is_reg_in_us_or_els = models.BooleanField() 
    brokerage = models.BooleanField() 
    nfa_by_law_1101 = models.BooleanField() 
    regulatory = models.BooleanField() 
    arbitrations = models.BooleanField() 
    investigations = models.BooleanField() 
    crime = models.BooleanField() 
    pol_mak_in_oth_com = models.BooleanField() 
    officer = models.BooleanField() 
    us_tax_classification = models.ForeignKey(us_tax_classifications, on_delete=models.CASCADE)
    formation_country = models.ForeignKey(countries, on_delete=models.CASCADE)
    exchange_traded_publicly = models.BooleanField()

class controlling_persons(models.Model):    
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    title = models.ForeignKey(salutations, on_delete=models.CASCADE)
    dir_own_vot_shr = models.FloatField()
    ind_own_vot_shr = models.FloatField()
    birthdate = models.DateField()
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    doc_issue_date = models.DateField()
    doc_expire_date = models.DateField()
    doc_issue_authority = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='cp_country')
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    tax_residency = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='cp_tax_residency')
    tax_id_no = models.CharField(max_length=30)
    additional_tax_residency = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='additional_tax_residency')
    additional_tax_id = models.CharField(max_length=30)
    con_com_reg_no = models.CharField(max_length=30)

class entity_consent(models.Model):
    submit_orders = models.ForeignKey(contact_methods, on_delete=models.CASCADE, related_name='ec_submit_orders')    
    submit_docs = models.ForeignKey(contact_methods, on_delete=models.CASCADE, related_name='submit_docs')
    form_w8bene = models.CharField(max_length=30)
    company_reg_no = models.CharField(max_length=30)

class representatives(models.Model):
    director = models.BooleanField()
    title_in_org = models.CharField(max_length=50)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    birthdate = models.DateField()
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    doc_type = models.ForeignKey(id_types, on_delete=models.CASCADE)
    doc_isse_date = models.DateField()
    doc_exp_date = models.DateField()
    doc_issuer = models.CharField(max_length=50)
    country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='r_country')
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    address = models.CharField(max_length=200)    
    phone = models.CharField(max_length=30)
    email = models.EmailField()    
    tax_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='r_tax_country')
    tax_id_no = models.CharField(max_length=30) 
    additional_tax_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='r_additional_tax_country')
    additional_tax_id = models.CharField(max_length=30)
    com_reg_no = models.CharField(max_length=30)     

class controlling_entities(models.Model):
    entity_name = models.CharField(max_length=50)
    controlling_shares = models.FloatField()
    email = models.EmailField()   
    phone = models.CharField(max_length=30)
    traded_on_exchange = models.BooleanField()
    lega_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='ce_lega_country')
    lega_state = models.CharField(max_length=50)
    lega_city = models.CharField(max_length=50)
    lega_zipcode = models.CharField(max_length=20)
    lega_address = models.CharField(max_length=200)      
    maa_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='ce_maa_country')
    maa_state = models.CharField(max_length=50)
    maa_city = models.CharField(max_length=50)
    maa_zipcode = models.CharField(max_length=20)
    maa_address = models.CharField(max_length=200)    
    tax_country = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='ce_tax_country')
    tax_id_no = models.CharField(max_length=30)      
    reg_no = models.CharField(max_length=30)   
    place_of_busines = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='place_of_business')
    con_com_reg_no = models.CharField(max_length=50)

class deal_types(models.Model):
    name = models.CharField(max_length=20)      

class order_types(models.Model):
    type = models.CharField(max_length=10)    
    full_name = models.CharField(max_length=20)
    desc = models.TextField()

class deal_sides(models.Model):
    code = models.CharField(max_length=20)    
    name = models.CharField(max_length=20)
    deal_type = models.ForeignKey(deal_types, on_delete=models.CASCADE)

class deal_subtypes(models.Model):
    name = models.CharField(max_length=20)    
    desc = models.CharField(max_length=30)
    deal_type = models.ForeignKey(deal_types, on_delete=models.CASCADE)
    investment = models.BooleanField()

class quantity_types(models.Model):
    type = models.CharField(max_length=30)   

class deal_statuses(models.Model):
    status = models.CharField(max_length=20)

class deals(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    value_startdate = models.DateField()
    value_enddate = models.DateField()
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)    
    account = models.ForeignKey(accounts, on_delete=models.CASCADE)
    account_type = models.ForeignKey(account_types, on_delete=models.CASCADE)
    deal_type = models.ForeignKey(deal_types, on_delete=models.CASCADE)
    deal_subtypes = models.ForeignKey(deal_subtypes, on_delete=models.CASCADE)
    deal_side = models.ForeignKey(deal_sides, on_delete=models.CASCADE)
    stock_exchange = models.ForeignKey(stock_exchanges, on_delete=models.CASCADE, related_name='stock_exchange')
    instrument = models.ForeignKey(instruments, on_delete=models.CASCADE)
    user = models.CharField(max_length=20) 
    deal_no = models.CharField(max_length=30) 
    status = models.CharField(max_length=10) 
    approxx_commission = models.DecimalField(max_digits=1000, decimal_places=2)
    order_no = models.CharField(max_length=20) 
    receipt_time = models.DateTimeField(auto_now=True)
    rec_method = models.ForeignKey(contact_methods, on_delete=models.CASCADE)
    currency = models.ForeignKey(currencies, on_delete=models.CASCADE)
    deal_type = models.ForeignKey(deal_types, on_delete=models.CASCADE)
    instrument = models.ForeignKey(instruments, on_delete=models.CASCADE)
    order_type = models.ForeignKey(order_types, on_delete=models.CASCADE)
    deal_side = models.ForeignKey(deal_sides, on_delete=models.CASCADE)
    limit_price = models.DecimalField(max_digits=1000000, decimal_places=2)
    stop_price = models.DecimalField(max_digits=1000000, decimal_places=2)
    quantity = models.DecimalField(max_digits=1000000, decimal_places=2)
    quantity_type = models.ForeignKey(quantity_types, on_delete=models.CASCADE)
    partial_fill = models.BooleanField()
    expire_date = models.DateField()
    gtc = models.BooleanField()
    custodian = models.ForeignKey(custodians, on_delete=models.CASCADE)
    counterparty = models.ForeignKey(counterparties, on_delete=models.CASCADE)
    exchange = models.ForeignKey(stock_exchanges, on_delete=models.CASCADE, related_name='exchange')
    portf_manager = models.CharField(max_length=20)
    market_type = models.BooleanField()
    compliance = models.BooleanField()
    execution_type = models.BooleanField()
    name = models.CharField(max_length=20) 
    position = models.CharField(max_length=20) 
    cash = models.CharField(max_length=20) 
    buying_power = models.CharField(max_length=20) 
    ones_order_form = models.FileField(upload_to='documents/')
    twos_order_form = models.FileField(upload_to='documents/')
    phone_record = models.FileField()
    ones_ord_form_svd_in_phs_fol = models.BooleanField()
    twos_ord_form_svd_in_phs_fol = models.BooleanField()
    send_time = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(deal_statuses, on_delete=models.CASCADE)
    status_change_date = models.DateTimeField() 







