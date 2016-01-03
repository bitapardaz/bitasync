import re
from subprocess import call
import datetime

def generate_bulk_licenses(user_pass_collection):

    #creating licenses in folder Licenses
    counter = 1
    for (username,password) in user_pass_collection:

        generate_one_license(username,password,counter)
        counter = counter + 1

    # zip folder Licenses given current data and time
    time_stamp = datetime.datetime.today().strftime("%B_%d_%Y_%H_%M_%S")
    output = 'Licenses_zip/Licenses_'
    output = output + time_stamp
    output = output + ".zip"
    command = ['zip', '-r', directory_path(output) , directory_path('Licenses')]
    call(command)

    # remove the individual license files
    location = directory_path('/Licenses/*')
    command = 'rm ' + location
    call(command,shell=True)

def generate_one_license(username,password,counter):

    # generate bulk_license_tmp.tex
    generate_latex_file(username,password)

    # run latex
    command = [ "pdflatex" , "-output-directory" ,  directory_path('')  ,  directory_path('bulk_license_tmp.tex')  ]
    call(command)

    # get the second page in the file
    outputname = "Licenses/"+ str(counter) + ".pdf"
    outputname = directory_path(outputname)
    command = ["pdftk", directory_path("bulk_license_tmp.pdf"), "cat", "2", "output", outputname]
    call(command)


def generate_latex_file(username,password):

    # read the file : bulk_license.tex
    st = open( directory_path('bulk_license.tex') , 'r' ).read()
    st2 = replace_username_password(st,username,password)

    new_file = open(  directory_path('bulk_license_tmp.tex') , 'w' )
    new_file.write(st2)
    new_file.close()

def replace_username_password(text,username,password):

    rep = {"Username": username, "Password": password}

    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return text

def directory_path(original_file):
    directory = 'shop_billing/bulk_license_generation_modules/'
    return directory+original_file
