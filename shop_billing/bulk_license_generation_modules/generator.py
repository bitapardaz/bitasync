import re
from subprocess import call

def generate_bulk_licenses(user_pass_collection):

    # creating licenses in folder Licenses
    counter = 1
    for (username,password) in user_pass_collection:

        generate_one_license(username,password,counter)
        counter = counter + 1

    # zip folder Licenses


    # send it by email to printing@gooshibegooshi.com




def generate_one_license(username,password,counter):

    # generate bulk_license_tmp.tex
    generate_latex_file(username,password)

    # run latex
    command = ["pdflatex","-output-directory", "code_test/bulk_license_generation_modules/","code_test/bulk_license_generation_modules/bulk_license_tmp.tex"]
    call(command)

    # get the second page in the file
#    outputname = "Licenses/"+ str(counter) + ".pdf"
#    command = ["pdftk", "bulk_license_tmp.pdf", "cat", "2", "output", outputname]
#    call(command)


def generate_latex_file(username,password):

    # read the file : bulk_license.tex
    st = open('code_test/bulk_license_generation_modules/bulk_license.tex','r').read()
    st2 = replace_username_password(st,username,password)

    new_file = open('code_test/bulk_license_generation_modules/bulk_license_tmp.tex','w')
    new_file.write(st2)
    new_file.close()

def replace_username_password(text,username,password):

    rep = {"Username": username, "Password": password}

    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return text
