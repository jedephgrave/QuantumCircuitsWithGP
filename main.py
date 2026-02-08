from gp import gp
from config import check_prob

def main():
    if check_prob: 
        p = gp.evolution()
        print(p)
    else:
        print("Check operation probabilities sum to 1")
    

if __name__ == "__main__":
    main()