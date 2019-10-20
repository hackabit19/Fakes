
import os

def run_all():
    #os.system("python '/home/pr7/Desktop/FlaskTryFirst/Self-Correction-Human-Parsing-master/evaluate.py' --dataset lip --restore-weight '/home/pr7/Desktop/FlaskTryFirst/Self-Correction-Human-Parsing-master/exp-schp-201908261155-lip.pth' --input '/home/pr7/Desktop/FlaskTryFirst/data/test/person' --output '/home/pr7/Desktop/FlaskTryFirst/data/test/person-parse'")

    #pose model
    #os.system("python ")

    #run_gmm model
    os.system("python run_gmm.py")

    #run_tom model
    os.system("python run_tom.py")
