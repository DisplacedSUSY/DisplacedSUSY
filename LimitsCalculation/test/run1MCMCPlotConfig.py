#!/usr/bin/env python

from DisplacedSUSY.Configuration.systematicsDefinitions import signal_cross_sections

intLumi = 19680 # MuEG 22Jan Rereco
energy = '8'

#masses = ['200','300','400','500','600','700','800','900']
masses = ['200']
#lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']
lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1']

# description of all the plots to be made
plotDefinitions = [

    {
        # this will be the name of the canvas in the output root file
        'title' : '8_TeV_MCMC_limits',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop c#tau [cm]',
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'energy' : '8'
                'source' : ['Run1_FinalResults_MCMC'],
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'legendEntry' : 'MCMC',
            },
        ],
    },

    ##################### EXAMPLE LIMIT PLOT VS. LIFETIME                          
     {                                
         'title' : 'limits_vs_lifetime',  
         'xAxisType' : 'lifetime',        
         'xAxisLabel' : 'Stop c#tau [cm]',                                   
         'graphs' : [                 
             {                        
                 'source' : ['Run1_FinalResults_MCMC'],                                 
                 'energy' : '8'
                 'mass' : '200',    
                 'colorScheme' : 'green',                                    
                 'graphsToInclude' : ['exp','obs'],                                
                 'legendEntry' : 'mass_{#tilde{t}} = 200 GeV',               
             },                       
             {                        
                 'source' : ['Run1_FinalResults_MCMC'],                                
                 'energy' : '8'
                 'mass' : '300',    
                 'colorScheme' : 'red',                                      
                 'graphsToInclude' : ['exp','obs'],                                
                 'legendEntry' : 'mass_{#tilde{t}} = 300 GeV',                 
             },                       
             {                        
                 'source' : ['Run1_FinalResults_MCMC'],                                
                 'energy' : '8'
                 'mass' : '400',   
                 'colorScheme' : 'blue',                                
                 'graphsToInclude' : ['exp','obs'],                                
                 'legendEntry' : 'mass_{#tilde{t}} = 400 GeV',                
             },                       
         ],                           
     },                               
    ##################### EXAMPLE LIMIT PLOT VS. MASS                          
     {                                
         'title' : 'limits_vs_mass',  
         'xAxisType' : 'mass',        
         'xAxisLabel' : 'Stop Mass [GeV]',                                   
         'graphs' : [                 
             {                        
                 'source' : ['Run1_FinalResults_MCMC'],                                 
                 'energy' : '8'
                 'lifetime' : '1',    
                 'colorScheme' : 'green',                                    
                 'graphsToInclude' : ['exp','obs'],                                
                 'legendEntry' : 'c#tau_{#tilde{t}} = 1 mm',               
             },                       
             {                        
                 'source' : ['Run1_FinalResults_MCMC'],                                
                 'energy' : '8'
                 'lifetime' : '10',    
                 'colorScheme' : 'red',                                      
                 'graphsToInclude' : ['exp','obs'],                                
                 'legendEntry' : 'c#tau_{#tilde{t}} = 10 mm',                 
             },                       
             {                        
                 'source' : ['Run1_FinalResults_MCMC'],                                
                 'energy' : '8'
                 'lifetime' : '100',   
                 'colorScheme' : 'blue',                                
                 'graphsToInclude' : ['exp','obs'],                                
                 'legendEntry' : 'c#tau_{#tilde{t}} = 100 mm',                
             },                       
         ],                           
     },                               

]


