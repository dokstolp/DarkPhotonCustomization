import FWCore.ParameterSet.Config as cms

def addSimHits(process):
    if hasattr(process,'g4SimHits'):
        # defined watches
        process.g4SimHits.Physics = cms.PSet(
            process.customPhysicsSetup,
            G4BremsstrahlungThreshold = cms.double(0.5), ## cut in GeV
            DefaultCutValue = cms.double(1.), ## cuts in cm,default 1cm
            CutsPerRegion = cms.bool(True),
            type = cms.string('SimG4Core/Physics/CustomPhysics'),
            GflashEcal = cms.bool(False),
            GflashHcal = cms.bool(False),
            RusRoElectronEnergyLimit  = cms.double(0.0),
            ElectronStepLimit         = cms.bool(False),
            ElectronRangeTest         = cms.bool(False),
            PositronStepLimit         = cms.bool(False),
            FlagFluo    = cms.bool(False),
        )	
        process.g4SimHits.G4Commands = cms.vstring('/tracking/verbose 0')

def customiseDarkPhotonSIM_1en0(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(1.E0)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_7en1(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(7.E-1)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_5en1(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(5.E-1)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_3en1(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(3.E-1)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_1en1(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(1.E-1)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_8en2(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(8.E-2)
         ) 
    addSimHits(process)
    return (process)
 
def customiseDarkPhotonSIM_6en2(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(6.E-2)
         ) 
    addSimHits(process)
    return (process)
 
def customiseDarkPhotonSIM_4en2(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(4.E-2)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_2en2(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(2.E-2)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_1en2(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(1.E-2)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_9en3(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(9.E-3)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_7en3(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(7.E-3)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_5en3(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(5.E-3)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_3en3(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(3.E-3)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_1en3(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(1.E-3)
         ) 
    addSimHits(process)
    return (process)

def customiseDarkPhotonSIM_1en4(process):
    process.customPhysicsSetup = cms.PSet( 
         particlesDef   = cms.FileInPath('SimG4Core/CustomPhysics/data/particle_darkphoton.txt'),
         dark_factor    = cms.double(1.E-4)
         ) 
    addSimHits(process)
    return (process)

