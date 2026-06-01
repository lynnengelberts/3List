""" 
Script to verify the time complexity of 3List, according to Theorem 3.1 
(arXiv/ePrint), respectively Theorem 1 (Proceedings of CRYPTO 2026). 
"""

from math import log2, cos, sin, acos, sqrt, pi 


def prob_cap(alpha):
    """
    Probability that a uniformly random unit vector lands in a fixed spherical cap of angle alpha. 

    Parameters
    ----------
    alpha : float
        Angle of spherical cap. 
    
    Returns
    -------
    float 
        Log_2 of the probability, divided by the dimension. 
    """
    return log2(1 - cos(alpha)**2)/2


def prob_wedge(alpha, beta, theta):  
    """
    Probability that a uniformly random unit vector lands in a fixed spherical wedge of angles 
    alpha and beta, defined by two unit vectors of angle theta. 

    Parameters
    ----------
    alpha, beta : float
        Angles of the intersecting spherical caps defining the wedge. 
    theta : float 
        Angle of the fixed unit vectors that define the caps.  
    
    Returns
    -------
    float 
        Log_2 of the probability, divided by the dimension. 
    """
    gamma_squared = (cos(alpha)**2 + cos(beta)**2 - 2*cos(alpha)*cos(beta)*cos(theta))/sin(theta)**2 
    return log2(1 - gamma_squared)/2


def time_3List(alpha, alpha_, size_L = log2(27/16)/4, theta = acos(1/3), theta_ = acos(1/sqrt(3))): 
    """
    Time complexity of 3List. 

    Parameters
    ----------
    alpha, alpha_ : float
        Angles used as 3List parameters. 
    theta, theta_ : float 
        Angles defining the solution set Tsol(L, theta, theta_). 
    size_L : float 
        Log_2 of the list size, divided by the dimension.  
    
    Returns
    -------
    float 
        Log_2 of the time complexity, divided by the dimension. 

    Raises 
    ------ 
    ValueError 
        If the conditions (*) in the proof of Theorem 3.1 (resp. Theorem 1 in the Proceedings version)
        are not satisfied. 
    """

    # Verify conditions (*)    
    if not all(0 < angle < pi/2 for angle in [theta, theta_, alpha, alpha_]): 
        raise ValueError("Angles must lie in (0, pi/2).")  
    if not (2*alpha > theta and 2*alpha_ > theta_):  
        raise ValueError("Wedge conditions not satisfied.") 
    if not (size_L + prob_cap(theta_) <= 0): 
        raise ValueError("Condition on theta_ not satisfied.")
    if not all(size_L + X > 0 for X in [prob_cap(alpha), 
                                        prob_cap(alpha_), 
                                        prob_wedge(theta, alpha, alpha), 
                                        size_L + prob_wedge(theta_, alpha_, alpha_)]): 
        raise ValueError("Other conditions on angles not satisfied.")
    
    # Log_2 of the parameter ell (divided by the dimension)
    ell = (prob_cap(alpha) - prob_wedge(alpha, alpha, theta) 
           + prob_cap(alpha_) - prob_wedge(alpha_, alpha_, theta_)) 
    
    # Log_2 of |Tsol(L, theta, theta_)| (divided by the dimension), according to the proof 
    size_Tsol = size_L 
    
    time_pre    = size_L 
    time_search = ((size_Tsol - ell)/2 
                   + max((size_L*2 + prob_cap(alpha))/2, 
                         (size_L*3 + prob_wedge(theta, alpha, alpha) + prob_cap(alpha_))/2)) 
    return ell + max(time_pre, time_search) 


if __name__ == "__main__":
    alpha  = acos(0.347606)
    alpha_ = acos(0.427124)
    
    t = time_3List(alpha, alpha_) 
    print(f"Time exponent: {t:.6f} (claimed exponent: 0.284551)") 
