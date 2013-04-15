#ifndef _KEPLER_
#define _KEPLER_

#include <fitsio.h>

#define KEPLER_LONG (0.0188194)

typedef struct {
    int length;
    float *time;
    float *flux;
    float *ferr;
    float *ivar;
} dataset;

dataset *init_dataset(int length);
void free_dataset(dataset *self);
int mask_dataset(dataset *self);

dataset *read_kepler_lc (const char *filename);

#endif
