/**
 *  main -
 *  @noOfKald: Number of kaleidoscopes
 *  @price_of_kald: Price of a unit kaleidoscope
 *  @tax: Value added tax for a unit kaleidoscope
 *  @discount: Discount applied to cost price if more than 0ne kaleidoscope is bought
 *  @total_calc_price: Total calculated price
 *  @discounted_price: Discounted price
 *  @taxed_price: Taxed price
 *  @total_price: Total cost price
 *
 *  Return: Always 0.
 */

#include <stdlib.h>
#include <stdio.h>
int main(void)
{
    /* Introducing Variables */
    int noOfKald;
    double price_of_kald = 5.00;
    double tax = 0.07;      /*	 Tax: 7% */
    double discount = 0.10; /* Discount: 10% */
    double total_calc_price;
    double discounted_price;
    double taxed_price;
    double total_price;

    /* This code stores the number of kaleidoscopes entered from standard input. */
    printf("Enter your desired number of kaleidoscopes: ");
    scanf("%d", &noOfKald);

    /* When the number of kaleidoscopes is greater than 1 */
    if (noOfKald > 1)
    {
        printf("You want to purchase %d kaleidoscopes\n", noOfKald);
        printf("Calculating your total cost......\n");

        /* Typecasting no_of_kald to an int */
        noOfKald = (int)noOfKald;

        /* Performing calculations.... */
        total_calc_price = noOfKald * price_of_kald;
        total_calc_price = (double)total_calc_price;

        /* Performing discounts... */
        discount = discount * total_calc_price; /* Calculating the discount */
        discount = (double)discount;

        /* Calculating the discounted price */
        discounted_price = total_calc_price - discount;
        discounted_price = (double)discounted_price; /* Typecasting */

        /* Calculating for tax */
        taxed_price = (tax * discounted_price) + discounted_price;
        taxed_price = (double)taxed_price;  /* Typecasting */

        /* Printing the final price */
        total_price = (double)taxed_price;
        printf("Your total cost is %.2f.\n", total_price);
    }

    /* When the number of kaleidoscopes is 1*/
    else if (noOfKald == 1)
    {
        printf("You want to purchase %d kaleidoscopes\n", noOfKald);
        printf("Calculating your total cost......\n");

        /* Typecasting no_of_kald to an int */
        noOfKald = (int)noOfKald;

        /* Performing calculations.... */
        total_calc_price = noOfKald * price_of_kald;
        total_calc_price = (double)total_calc_price;

        /* Calculating for tax */
        taxed_price = (tax * total_calc_price) + total_calc_price;
        taxed_price = (double)taxed_price;  /* Typecasting */

        /* Printing the final price */
        total_price = (double)taxed_price;
        printf("Your total cost is %.2f.\n", total_price);
    }

    else
    {
        printf("You entered an invalid number.\n");
    }

    return (0);
}

/**
 * Problem 1: You sell souvenir kaleidoscopes at a gift shop and if a customer buys more than one, they get a 10% discount on all of them!
 * Given that the total number of kaleidoscopes that a customer buys, let them know what their total will be. Tax is 7%.
 * All of your kaleidoscopes cost the same amount, 5.00
 *
 * Task: Take the number of kaleidoscopes that a customer buys and output their total cost including tax and any discounts.
 *
 * Input format: An integer value that represents the number of kaleidoscopes that a customer needs
 *
 * Output Format: A number that represents the total purchase price of decimal prices.
 */

