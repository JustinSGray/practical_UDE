def babylonian_sqrt(a): 
    x_n = a
    resid = x_n*x_n - a
    iter_count = 0
    while resid > 1e-3 and iter_count < 15: 
      x_n1 = 0.5*(a/x_n+x_n)
      resid = x_n1*x_n1 - a
      x_n = x_n1
      iter_count += 1 
    return x_n, iter_count


test = 600

b_sqrt, counter = babylonian_sqrt(test)
real_sqrt = test**0.5

print(counter, b_sqrt, real_sqrt)

def composite_f1(a):
  sqrt_a = a**0.5
  return 2*sqrt_a + 1/sqrt_a

def composite_f2(a):
  sqrt_a, iter_count = babylonian_sqrt(a)
  return 2*sqrt_a + 1/sqrt_a

print(composite_f1(600.32))
print(composite_f2(600.32))


def d_composite_f1(a): 
    sqrt_a = a**0.5
    d_sqrt_a = 0.5*a**-0.5
    return (2 - 1/sqrt_a**2)*d_sqrt_a


def d_composite_f2(a): 
    sqrt_a, d_sqrt_a, d_iter_count = d_babylonian_sqrt(a)
    return (2 - 1/sqrt_a**2)*d_sqrt_a



def d_babylonian_sqrt(a):
    x_n = a

    resid = x_n*x_n - a
    iter_count = 0
    
    while resid > 1e-3 and iter_count < 15: 
      x_n1 = 0.5*(a/x_n+x_n)
      d_x_n1 = 0.5*(1/x_n)
      
      resid = x_n*x_n - a
      x_n = x_n1
      iter_count += 1 
    return x_n1, d_x_n1, iter_count


def d_composite_f2_implicit(a): 
    sqrt_a, d_sqrt_a = d_babylonian_sqrt_implicit(a)
    return (2 - 1/sqrt_a**2)*d_sqrt_a


def d_babylonian_sqrt_implicit(a): 
    x_n1, iter_count = babylonian_sqrt(a)

    resid = x_n1*x_n1 - a
    dresid__da = - 1
    dresid__dx_n = 2*x_n1 

    return x_n1, -dresid__da/dresid__dx_n



print(composite_f1(600.32+1e-50j).imag/1e-50)
print(d_composite_f1(600.32))
print(d_composite_f2(600.32))
print(d_composite_f2_implicit(600.32))
print()
print()


# primary implicit function definition
def resid_babylonian_sqrt(a, sqrt_a): 
      resid = x_n*x_n - a
      return 

# separate method for converging the implicit function
def solve_babylonian_sqrt(a): 
    sqrt_a_guess = a
    resid = resid_babylonian_sqrt(a, sqrt_a_guess)
    iter_count = 0
    while resid > 1e-3 and iter_count < 15: 
      iter_count += 1 
      next_guess = 0.5*(a/sqrt_a_guess+sqrt_a_guess)
      resid = resid_babylonian_sqrt(a, next_guess)
      sqrt_a_guess = next_guess
    return x_n, iter_count


