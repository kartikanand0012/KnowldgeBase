# Notes

## scaler-prob-29028

- **We only checkup to 6 for a number like 36 becasuse while fin** (2026-07-22): We only checkup to 6 for a number like 36 becasuse while finding Factors we usually don't have to check all the way upto n as after some time the pattern start repeating it self so if we have two check that is 1. A is divisble by i and what number comes when i divide A these both numbers are factor of A similary if a numbers like 36 we have 9 factors we need 2nd check that is if  A is divisble by i we add two but if that i * i is equal to A then we have to add 1 this is the core logic and because of this we dont have to iterate till n instead we can iterate till root n which significantly optimize the performance
