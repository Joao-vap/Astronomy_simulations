class Quaternion:

    """ Quaternion is a class defined to comport a type of number with four dimensions

    Quaternions have very particular multiplications and are not commutable. Very often
    used for rotations in Computation.

    Properties
    ----------
    self.real : float, int
        real part of quaternion
    self.i : float, int
        i - imaginary term of quaternion
    self.j : float, int
        j - imaginary term of quaternion
    self.k : float, int
        k - imaginary term of quaternion


    Attributes
    ----------
    self._real : float, int
        real part of quaternion
    self._i : float, int
        i - imaginary term of quaternion
    self._j : float, int
        j - imaginary term of quaternion
    self._k : float, int
        k - imaginary term of quaternion
    self._module: float, int
        module of quaternion

    Methods
    -------
    __str__(self)
        returns the string associated with the values for the quaternion

    __repr__(self)
        returns a representation of the quaternion

    get(self)
        returns a tuple associated with the quaternion

    __add__(self, other)
        implements and return addition for two quaternions

    __sub__(self, other)
        implements and return subtraction for two quaternions

    __truediv__(self, other)
        implements and return division for two quaternions

    __mul__(self, other)
        implements and return multiplication for two quaternions

    __rmul__(self, other)
        implements and return multiplication for two quaternions
        when quaternion is on the right

    __eq__(self, other)
        Compares two Quaternions in terms of equality
        comparing term by term

    __lt__(self, other)
        Compares two Quaternions for 'less than'
        comparing by module

    __lt__(self, other)
       Compares two Quaternions for 'less than or equals'
       comparing by module

    __abs__(self)
        Returns module of quaternion

    conjugate(self)
        returns the conjugate of the self

    conjugate_multiplicate(self)
        returns the multiplication of the self times its conjugate

    inverse(self)
        returns the inverse of the self

    set_real(self, value)
        sets component of quaternion with 'value'

    set_i(self, value)
        sets component of quaternion with 'value'

    set_j(self, value)
        sets component of quaternion with 'value'

    set_k(self, value)
        sets component of quaternion with 'value'
    """

    def __init__(self, real, i, j, k):

        """
        Parameters
        ----------
        real : float
            _real term of quaternion
        i : float
            _i - imaginary term of quaternion
        j : float
            _j - imaginary term of quaternion
        k : float
            k - imaginary term of quaternion
        """
        self._real = real
        self._i = i
        self._j = j
        self._k = k
        self._module = self.__abs__()

    def __str__(self):

        """Returns the vector in a string """

        return f'{self._real} + {self._i} i + {self._j} j + {self._k} k'

    def __repr__(self):

        """Returns the representation of the vector"""

        return f'Quaternion({self._real}, {self._i}, {self._j}, {self._k})'

    def get(self):

        """Returns vector in a tuple form"""

        return self._real, self._i, self._j, self._k

    def __add__(self, other):

        """Defines the sum of two quaternions

        Parameters
        ----------

        other : Quaternion
            The vector to which we sum the self

        """

        if isinstance(other, Quaternion):

            real = self._real + other._real
            imag_i = self._i + other._i
            imag_j = self._j + other._j
            imag_k = self._k + other._k

            return Quaternion(real, imag_i, imag_j, imag_k)

        else:
            return self + other

    def __sub__(self, other):

        """Defines the subtraction of two quaternions

        Parameters
        ----------

        other : Quaternion
            The vector to which we subtract the self

        """

        if isinstance(other, Quaternion):

            real = self._real - other._real
            imag_i = self._i - other._i
            imag_j = self._j - other._j
            imag_k = self._k - other._k

            return Quaternion(real, imag_i, imag_j, imag_k)

        else:
            return self - other

    def __mul__(self, other):

        """Defines the multiplication of two quaternions

        Parameters
        ----------

        other : Quaternion, int, float
            The vector to which we multiply the self

        """

        if isinstance(other, Quaternion):
            real = (self._real * other._real - self._i * other._i - self._j * other._j - self._k * other._k)
            imag_i = (self._real * other._i + self._i * other._real + self._j * other._k - self._k * other._j)
            imag_j = (self._real * other._j - self._i * other._k + self._j * other._real + self._k * other._i)
            imag_k = (self._real * other._k + self._i * other._j - self._j * other._i + self._k * other._real)

            return Quaternion(real, imag_i, imag_j, imag_k)

        else:
            return Quaternion(self._real * other, self._i * other, self._j * other, self._k * other)

    def __rmul__(self, other):

        """Defines the multiplication when quaternion on right

        Parameters
        ----------

        other : float, int
            The quaternion to which we multiply the self
        """

        return self.__mul__(other)

    def __truediv__(self, other):

        """Defines the division of two quaternions

        Parameters
        ----------

        other : Quaternion
            The vector to which we divide the self

        """    

        if isinstance(other, Quaternion):

            value = (self * other) * (1 / other.conjugate_multiplicate())

            return Quaternion(value._real, value._i, value._j, value._k)
        
        else:
            return self / other

    def __eq__(self, other):

        """Compares two quaternions and check for equality

        Parameters
        ----------

        other : Quaternion
            The vector to which we compare the self
        """

        if isinstance(other, Quaternion):

            if self._real == other._real and self._i == other._i and self._j == other._j and self._k == other._k:
                equals = True
            else:
                equals = False

            return equals

        else:
            raise TypeError(f"Cannot compare '{type(self)}' with '{type(other)}' ")

    def __lt__(self, other):

        """Compares two quaternions modules and check for 'less than'

        Parameters
        ----------

        other : Quaternion
            The vector to which we compare the self

        """
        if isinstance(other, Quaternion):

            return self._module < other._module

        else:
            raise TypeError(f"Cannot compare '{type(self)}' with '{type(other)}' ")

    def __le__(self, other):

        """Compares two quaternions modules and check for 'less than or equal'

        Parameters
        ----------

        other : Quaternion
            The vector to which we compare the self

        """
        if isinstance(other, Quaternion):

            return self._module <= other._module

        else:
            raise TypeError(f"Cannot compare '{type(self)}' with '{type(other)}' ")

    def __abs__(self):

        """Returns module of quaternion
        rounded to the sixth decimal
        """

        return round((self.conjugate_multiplicate()) ** 0.5, 6)

    def conjugate(self):

        """Gives the conjugate quaternion of self """

        return Quaternion(self._real, -self._i, -self._j, -self._k)

    def conjugate_multiplicate(self):

        """Defines the multiplication of two quaternions, but conjugates

        Possible to use __mul__ but more exact as all imaginary components vanish,
        that may not happen if we have rounding errors. There are no parameters as
        we can calculate it with only the self.

        """

        return self._real ** 2 + self._i ** 2 + self._j ** 2 + self._k ** 2

    def inverse(self):

        """ Defines the inverse of a Quaternion """
        value = self.conjugate() * (1 / self.conjugate_multiplicate())

        return Quaternion(value._real, value._i, value._j, value._k)

    def set_real(self, value):

        """Sets the real value in quaternion

        Parameters
        ----------

        value : float, int
            value to which we set the component
        """
        if isinstance(value, int) or isinstance(value, float):
            self._real = value

        else:
            raise ValueError(f"Cannot attribute '{type(value)}' to Quaternion ")

    def set_i(self, value):

        """Sets the i - imaginary value in quaternion

        Parameters
        ----------

        value : float, int
            value to which we set the component
        """

        if isinstance(value, int) or isinstance(value, float):
            self._i = value

        else:
            raise ValueError(f"Cannot attribute '{type(value)}' to Quaternion ")

    def set_j(self, value):

        """Sets the j - imaginary value in quaternion

        Parameters
        ----------

        value : float, int
            value to which we set the component
        """

        if isinstance(value, int) or isinstance(value, float):
            self._j = value

        else:
            raise ValueError(f"Cannot attribute '{type(value)}' to Quaternion ")

    def set_k(self, value):

        """Sets the k - imaginary value in quaternion

        Parameters
        ----------

        value : float, int
            value to which we set the component
        """

        if isinstance(value, int) or isinstance(value, float):
            self._k = value

        else:
            raise ValueError(f"Cannot attribute '{type(value)}' to Quaternion ")

    real = property(None, set_real, None, 'Real part of quaternion')
    i = property(None, set_i, None, 'i - imaginary part of quaternion')
    j = property(None, set_j, None, 'j - imaginary part of quaternion')
    k = property(None, set_k, None, 'k - imaginary part of quaternion')
