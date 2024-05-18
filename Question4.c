/*
    This code generated the exponentially distributed random numbers from
    uniformly distributed random numbers using transformation method. Then
    it stores the sample in the file 'exponential_samples.txt'.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Defining the sample size
#define NUM_SAMPLES 10000 

// Using transformation method to generate exponentially distributed random variables
double generate_exponential(double mean) {
    double u = (double)rand() / RAND_MAX;
    return -log(u) * mean;
}

int main() {
    double samples[NUM_SAMPLES];
    double mean = 0.5; // mean of the exponential distribution
    srand((unsigned)time(NULL)); // Seeding the random number generator

    for (int i = 0; i < NUM_SAMPLES; i++) {
        samples[i] = generate_exponential(mean); // Generating exponentially distribute random numbers
    }

    // Writing the samples to a file
    FILE *file = fopen("exponential_samples.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    for (int i = 0; i < NUM_SAMPLES; i++) {
        fprintf(file, "%f\n", samples[i]);
    }
    fclose(file);
    return 0;
}
