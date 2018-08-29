'''
Created on 29 Aug 2018

@author: ID121943
'''
import os


def main():
    # my code here
    print __file__
    print os.path.dirname(__file__)
    print os.path.join(os.path.dirname(__file__), '..')
    print os.path.dirname(os.path.realpath(__file__))
    print os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    main()
    
