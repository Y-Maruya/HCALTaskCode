# HCALTaskCode

## Configuration Settings

The system is currently configured to use settings from `cfgFiles/HL_thrOpt3_HVOptValidModSelectThr1023_delay54` (the configuration we used before July 1st).

When you execute `python3 test.py`, it generates configuration files in the directory `cfgFiles/HL_thrOpt3_thOffset_*_HVOptValidModSelectThr1023`.

* is offset for threshold.

## Technical Notes

- [SPIROC datasheet](https://indico.cern.ch/event/232082/contributions/493652/attachments/385835/536707/Spiroc2_userGuide2009_datasheet.pdf)
- According to the datasheet, the threshold slope has a negative value to the voltage.