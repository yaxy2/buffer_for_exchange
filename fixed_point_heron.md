# Softwarepraktikum Notes
## Wurzelziehen mit Fixed Point Arithmetik via Heron Verfahren

```c
#include <sysc/datatypes/fx/sc_fixed.h>
#include <systemc>
#include <stdio.h>

#define WL 16
#define IWL 8
#define SC_INCLUDE_FX

using namespace sc_dt;
using namespace std;


typedef sc_fixed<WL, IWL> fixed_t;


fixed_t fixed_heron_sqrt(fixed_t s) {

  fixed_t x = s/2;
  fixed_t x_n;
  
  while(true) {
    x_n = (x + s / x) / 2;

    fixed_t diff = x - x_n;
    if(diff < 0) {
      diff = -diff;
    }

    fixed_t e = fixed_t(1.0/(1<<(WL-IWL-2)));
    if (diff < e){
      break;
    }
    x = x_n;
  }

  return x_n;
  
  
}

int sc_main(int argc, char* argv[]){

  fixed_t s = 5;
  fixed_t res = fixed_heron_sqrt(s);

  cout << res << endl;
  
  return 0;

}
```
