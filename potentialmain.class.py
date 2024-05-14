
#-----------------------------------------
#   I M P O R T S
#-----------------------------------------


import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike


class Potential:
    def __init__(self,*args: float):
        self.coefficients=args


    def f(self,x: ArrayLike):
        #to calculate the potential function,which will be overridden by subclasses
        raise NotImplementedError("subclass must  be implemented abstract method")

    # --------------------------------------------------------------------------
    #   analytical derivative that  need to be implemented in the child classes
    # --------------------------------------------------------------------------
    def analytical_derivative(self, x: ArrayLike)->ArrayLike:
        raise NotImplementedError("subclass must  be implemented abstract method")

    # ---------------------------------------------------------------------
    #    numerical derivative that are passed to the child classes
    # ---------------------------------------------------------------------
    def numerical_derivative(self, x: ArrayLike, h=0.0001):
        """
        define numerical derivative
        Args:
            x: x_values
            h:spacing of the finite different point along x

        Returns:numerical derivative using the equation

        """

        return (self.f(x+h)-self.f(x-h))/(2*h)


    def plot_function(self,x_values)-> None:
         """
         plot the potential function over a given range of x values
         """


         y_values = self.f(x_values)
         dy_analytical = self.analytical_derivative(x_values)
         dy_numerical = self.numerical_derivative(x_values)

         plt.plot(x_values, y_values, label="f(x)", color="blue", linewidth=2, marker=".", markerfacecolor="k",
                  markersize=4)

         plt.plot(x_values, dy_analytical, label="f'(x) - analytical", color="red", linewidth=2, marker=".", markerfacecolor="k",
                  markersize=4)
         plt.plot(x_values, dy_numerical, label="f'(x) - numerical", color="green", linewidth=2, marker=".",
                  markerfacecolor="k",
                  markersize=4)


         plt.title(f"{self.__class__.__name__}  and Derivatives Plot")

         plt.xlabel("x")
         plt.ylabel("f(x)/f'(x)")
         plt.savefig(f"{self.__class__.__name__} and Derivatives fig.pdf")
         plt.legend()
         plt.show()

class Linear_Potential(Potential):
    def f(self, x: ArrayLike)-> ArrayLike:
        """
         calculate the linear potential
            Args:

                x:x_value

            Returns:linear potential for all x

        """
        m, c = self.coefficients
               #m: slope of the line, c:intercept of the line

        return m * x + c


    def analytical_derivative(self,x: ArrayLike):
        """
        calculate the  analytical derivative of a linear function
            Args:
                x: x_value

            Returns:analytical derivative m

        """
        m ,_ = self.coefficients
            #m:float, slope of the line
        return  np.full_like(x, m)


class Quadratic_Potential(Potential):
    def f(self, x: ArrayLike)-> ArrayLike:
        """
        calculate the quadratic potential
             Args:
                x: x_value

             Returns:quadratic potential

        """

        a, b, c = self.coefficients
            #a:float,   coefficients
            #b:float,   coefficients
            #c:float,   coefficients
        return a * x**2 + b * x + c

    def analytical_derivative(self,x: ArrayLike):
        """
        calculate the analytical derivative of a quadratic potential
            Args:
                x: x_value

            Returns:analytical derivative 2ax+b

        """
        a,b,_= self.coefficients
        return a * 2 * x + b
class DoubleWell_Potential(Potential):
    def f(self, x: ArrayLike)-> ArrayLike:
        """
        calculate the double well potential
            Args:
                x: x_value

            Returns:double well potential

        """
        a, b, c = self.coefficients
           # a:float,   coefficients
           # b:float,   coefficients
           # c:float,   coefficients
        return a * x**4 - b * x**2 + c

    def analytical_derivative(self,x: ArrayLike):
        """
        calculate the analytical derivative of double well potential
            Args:
                x: x_value

            Returns:analytical derivative 4ax^3-2bx

        """
        a,b,_= self.coefficients
           # a:float,   coefficients
           # b:float,   coefficients
        return a * 4 * x ** 3 - b * 2 * x

linear = Linear_Potential(2, -3)# linear potential with m=2,c=-3
linear.plot_function(np.linspace(-10,10,100))
quadratic = Quadratic_Potential(1, -5, 6)  # Quadratic potential with a=1, b=-5, c=6
quadratic.plot_function(np.linspace(-10,15,100))
doublewell = DoubleWell_Potential(1,2,-1)#double well potential with a=1,b=2,c=-1
doublewell.plot_function(np.linspace(-1.5,1.5,100))