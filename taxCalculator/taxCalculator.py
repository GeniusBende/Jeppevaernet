# Jeppe Skovby Bjørn
#
# Created using python version 3.8.8

import argparse

def print_args(args):
    print()
    print('Calculating using the following values:')
    print('AM percentage:\t\t' + '%5.0f' % (args.am * 100) + ' %')
    print('Tax:\t\t\t' + '%5.0f' % (args.tax * 100) + ' %')
    print('Personal allowance:\t' + '%8.2f' % args.pa)
    print('Income:\t\t\t' + '%8.2f' % args.income)
    print()

def calculate(args):
    args.am = args.income * args.am
    args.taxable_income = args.income - args.am - args.pa
    args.total_tax = args.taxable_income * args.tax
    args.paid_out = args.income - args.am - args.total_tax

    return args

def print_results(args):
    print()
    print('AM:\t\t\t' + '%8.2f' % args.am)
    print('Taxable income:\t\t' + '%8.2f' % args.taxable_income)
    print('Total tax:\t\t' + '%8.2f' % args.total_tax)
    print()
    print('Payment:\t\t' + '%8.2f' % args.paid_out)
    print()
    input('Pres enter to terminate...')

def main():
    argparser = argparse.ArgumentParser(
        description='Tax calculator for danish income'
    )
    argparser.add_argument(
        '-i', '--income',
        default=25000,
        type=float,
        help='The amount of income you get (default: 25000)'
    )
    argparser.add_argument(
        '-t', '--tax',
        default=0.38,
        type=float,
        help='The tax percentage (default: 0.38 -> 38)'
    )
    argparser.add_argument(
        '--pa',
        default=46600 / 12,
        type=float,
        help='The personal allowance aka the money you don\'t pay taxes from (default: 3883.3)'
    )
    argparser.add_argument(
        '--am',
        default=0.08,
        type=float,
        help='Employment contribution in percentage, AM in danish (default: 0.08 -> 8)'
    )
    args = argparser.parse_args()

    if args.income == 25000:
        print('Warning! No income provided. Using default income: ' + str(args.income))
        print('If help is needed, run program with -h for help')

    print_args(args)

    args = calculate(args)

    print_results(args)

if __name__ == '__main__':
    main()