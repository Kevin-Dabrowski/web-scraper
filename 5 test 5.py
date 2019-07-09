import requests
import re                   #replace betweeen 2 strings
from bs4 import BeautifulSoup
import ast                  #cant remember why imported
import pandas as pd         #for transposing csv
import csv                  #for transposing csv
import itertools            #this works
#from itertools import izip  #this doesnt work because it cant fint izip but can zip?


# get webpage in html (im also goin to make this a loop for one file for all the data)
Symbol = ["AAB", "AAV", "ABT", "ABX", "AC", "ACB", "ACB.WT", "ACD", "ACD.DB", "ACI", "ACO.X", "ACO.Y", "ACQ", "ACR.UN", "ACZ.UN", "AD", "ADN", "ADVZ", "ADVZ.U", "ADW.A", "ADW.B", "AEF", "AEF.WT", "AEM", "AEZS", "AFN", "AFN.DB.B", "AFN.DB.C", "AFN.DB.D", "AFN.DB.E", "AGF.B", "AGI", "AGT", "AGT.PR.A", "AHY.UN", "AI", "AI.DB", "AI.DB.A", "AI.DB.B", "AI.DB.C", "AI.DB.D", "AIF", "AII", "AIM", "AIM.PR.A", "AIM.PR.B", "AIM.PR.C", "AJX", "AKG", "AKT.A", "AKT.B", "AKU", "AKU.U", "ALA", "ALA.PR.A", "ALA.PR.B", "ALA.PR.E", "ALA.PR.G", "ALA.PR.I", "ALA.PR.K", "ALA.PR.U", "ALB", "ALB.PR.C", "ALC", "ALC.DB.A", "ALO", "ALS", "ALS.PR.A", "ALYA", "AMM", "ANX", "AOI", "AP.UN", "APHA", "APR.UN", "APS", "APY", "AQA", "AQN", "AQN.PR.A", "AQN.PR.D", "AQY.A", "AQY.WT", "AR", "ARE", "ARE.DB.C", "ARG", "ARX", "ASM", "ASM.WT", "ASND", "ASND.WT", "ASO", "ASP", "ASP.WT", "ASR", "ATA", "ATD.A", "ATD.B", "ATH", "ATL", "ATP", "ATP.DB.D", "ATP.DB.E", "ATZ", "AUG", "AUMN", "AUP", "AVL", "AVP", "AW.UN", "AX.PR.A", "AX.PR.E", "AX.PR.G", "AX.PR.I", "AX.UN", "AXR", "AYM", "AZP.PR.A", "AZP.PR.B", "AZP.PR.C", "AZZ", "BAD", "BAM.A", "BAM.PF.A", "BAM.PF.B", "BAM.PF.C", "BAM.PF.D", "BAM.PF.E", "BAM.PF.F", "BAM.PF.G", "BAM.PF.H", "BAM.PF.I", "BAM.PF.J", "BAM.PR.B", "BAM.PR.C", "BAM.PR.E", "BAM.PR.G", "BAM.PR.K", "BAM.PR.M", "BAM.PR.N", "BAM.PR.R", "BAM.PR.S", "BAM.PR.T", "BAM.PR.X", "BAM.PR.Z", "BANK", "BAR", "BB", "BB.DB.V", "BBD.A", "BBD.B", "BBD.PR.B", "BBD.PR.C", "BBD.PR.D", "BBL.A", "BBU.UN", "BCB", "BCE", "BCE.PR.A", "BCE.PR.B", "BCE.PR.C", "BCE.PR.D", "BCE.PR.E", "BCE.PR.F", "BCE.PR.G", "BCE.PR.H", "BCE.PR.I", "BCE.PR.J", "BCE.PR.K", "BCE.PR.L", "BCE.PR.M", "BCE.PR.N", "BCE.PR.O", "BCE.PR.Q", "BCE.PR.R", "BCE.PR.S", "BCE.PR.T", "BCE.PR.Y", "BCE.PR.Z", "BCI", "BDI", "BDIV", "BDT", "BEI.UN", "BEK.B", "BEP.PR.E", "BEP.PR.G", "BEP.PR.I", "BEP.PR.K", "BEP.PR.M", "BEP.UN", "BFIN", "BGC", "BGI.UN", "BGU", "BGU.U", "BHC", "BIK.PR.A", "BIP.PR.A", "BIP.PR.B", "BIP.PR.C", "BIP.PR.D", "BIP.PR.E", "BIP.PR.F", "BIP.UN", "BIR", "BIR.PR.A", "BIR.PR.C", "BK", "BK.PR.A", "BKCH", "BKCH.U", "BKI", "BKL.C", "BKL.F", "BKL.U", "BKX", "BL.UN", "BLB.UN", "BLCK", "BLDP", "BLU", "BLX", "BLX.DB.A", "BMO", "BMO.PR.A", "BMO.PR.B", "BMO.PR.C", "BMO.PR.D", "BMO.PR.E", "BMO.PR.Q", "BMO.PR.S", "BMO.PR.T", "BMO.PR.W", "BMO.PR.Y", "BMO.PR.Z", "BNC", "BND", "BNE", "BNG", "BNP", "BNS", "BNS.PR.D", "BNS.PR.E", "BNS.PR.F", "BNS.PR.G", "BNS.PR.H", "BNS.PR.I", "BNS.PR.Y", "BNS.PR.Z", "BOS", "BOY", "BPF.UN", "BPO.PR.A", "BPO.PR.C", "BPO.PR.E", "BPO.PR.G", "BPO.PR.I", "BPO.PR.N", "BPO.PR.P", "BPO.PR.R", "BPO.PR.S", "BPO.PR.T", "BPO.PR.W", "BPO.PR.X", "BPO.PR.Y", "BPRF", "BPS.PR.A", "BPS.PR.B", "BPS.PR.C", "BPS.PR.U", "BPY.UN", "BR", "BRB", "BRE", "BRF.PR.A", "BRF.PR.B", "BRF.PR.C", "BRF.PR.E", "BRF.PR.F", "BRY", "BSC", "BSC.PR.C", "BSD.PR.A", "BSD.UN", "BSO.UN", "BSX", "BTB.DB.E", "BTB.DB.F", "BTB.UN", "BTE", "BTO", "BU", "BUA.UN", "BUI", "BXE", "BXE.DB", "BXF", "BXS.DB.C", "BYD.UN", "BYL", "BYL.DB", "CACB", "CAE", "CAFR", "CAGG", "CAGS", "CAL", "CALL", "CALL.B", "CAN", "CAPS", "CAPS.B", "CAPS.U", "CAR.UN", "CARS", "CARS.B", "CARS.U", "CAS", "CBH", "CBL", "CBO", "CBT.UN", "CCA", "CCI.UN", "CCL.A", "CCL.B", "CCM", "CCO", "CCS.PR.C", "CCX", "CCZ", "CCZ.PR.A", "CDAY", "CDD.UN", "CDH", "CDV", "CDZ", "CED", "CEE", "CEF", "CEF.U", "CERV", "CES", "CES.B", "CES.U", "CET", "CEU", "CEW", "CF", "CF.DB.A", "CF.PR.A", "CF.PR.C", "CFF", "CFP", "CFW", "CFX", "CG", "CGG", "CGI", "CGI.PR.D", "CGL", "CGL.C", "CGO", "CGR", "CGT", "CGX", "CGY", "CHB", "CHE.DB.B", "CHE.DB.C", "CHE.DB.D", "CHE.UN", "CHH", "CHNA.B", "CHP.UN", "CHR", "CHR.DB", "CHW", "CIA", "CIC", "CIF", "CIGI", "CIQ.UN", "CIU.PR.A", "CIU.PR.C", "CIX", "CJ", "CJ.DB", "CJR.B", "CJT", "CJT.A", "CJT.DB.C", "CJT.DB.D", "CKE", "CKI", "CLF", "CLG", "CLIQ", "CLIQ.DB", "CLQ", "CLR", "CLS", "CM", "CM.PR.O", "CM.PR.P", "CM.PR.Q", "CM.PR.R", "CM.PR.S", "CM.PR.T", "CMCE", "CMG", "CMH", "CMMC", "CMR", "CMUE", "CMUE.F", "CNE", "CNL", "CNQ", "CNR", "CNT", "CNU", "COG", "COMM", "COP", "CORP", "CORV", "COW", "CP", "CPD", "CPG", "CPH", "CPI", "CPX", "CPX.PR.A", "CPX.PR.C", "CPX.PR.E", "CPX.PR.G", "CPX.PR.I", "CQE", "CR", "CRDL", "CRDL.WT", "CRH", "CRON", "CRP", "CRR.UN", "CRT.UN", "CRWN", "CRWN.DB", "CS", "CSD", "CSE.PR.A", "CSH.UN", "CSM", "CSU", "CSU.DB", "CSW.A", "CSW.B", "CSY", "CTC", "CTC.A", "CTF.UN", "CTX", "CU", "CU.PR.C", "CU.PR.D", "CU.PR.E", "CU.PR.F", "CU.PR.G", "CU.PR.H", "CU.PR.I", "CU.X", "CUD", "CUF.UN", "CUP.U", "CVD", "CVE", "CVG", "CWB", "CWB.PR.B", "CWB.PR.C", "CWB.PR.D", "CWI", "CWL", "CWW", "CWX", "CWX.NT.A", "CXF", "CXI", "CXN", "CYB", "CYBR", "CYBR.B", "CYH", "D.UN", "DANC", "DBO", "DC.A", "DC.PR.B", "DC.PR.D", "DC.PR.E", "DC.WT", "DCC", "DCF", "DCG", "DCM", "DCP", "DCS", "DCU", "DEE", "DEE.NT", "DEE.WT", "DF", "DF.PR.A", "DFC", "DFD", "DFE", "DFN", "DFN.PR.A", "DFU", "DGC", "DGR", "DGR.B", "DGRC", "DGS", "DGS.PR.A", "DHX", "DHX.DB", "DIAM", "DII.A", "DII.B", "DII.DB.U", "DIR.UN", "DISC", "DIV", "DIV.DB", "DIVS", "DLR", "DLR.U", "DML", "DNG", "DNT", "DOL", "DOO", "DPM", "DQD", "DQI", "DR", "DR.DB.A", "DRA.UN", "DRCU", "DRFC", "DRFD", "DRFU", "DRG.UN", "DRM", "DRM.PR.A", "DRMC", "DRMU", "DRT", "DRX", "DS", "DSG", "DXB", "DXC", "DXF", "DXG", "DXI", "DXM", "DXO", "DXP", "DXU", "DXV", "DXZ", "E", "EARN", "EBC.UN", "ECA", "ECF.UN", "ECN", "ECN.PR.A", "ECN.PR.C", "ECO", "ECS", "ECS.WT", "EDGE", "EDGF.UN", "EDR", "EDT", "EDV", "EF.UN", "EFH", "EFL", "EFN", "EFN.DB", "EFN.DB.A", "EFN.PR.A", "EFN.PR.C", "EFN.PR.E", "EFN.PR.G", "EFN.PR.I", "EFR", "EFR.DB", "EFR.WT", "EFX", "EGIF", "EGL", "EHE", "EHE.B", "EIF", "EIF.DB.G", "EIF.DB.H", "EIF.DB.I", "EIF.DB.J", "EIT.PR.A", "EIT.PR.B", "EIT.UN", "ELD", "ELF", "ELF.PR.F", "ELF.PR.G", "ELF.PR.H", "ELR", "ELV", "EMA", "EMA.PR.A", "EMA.PR.B", "EMA.PR.C", "EMA.PR.E", "EMA.PR.F", "EMA.PR.H", "EML.PR.A", "EMP.A", "EMV.B", "ENB", "ENB.PF.A", "ENB.PF.C", "ENB.PF.E", "ENB.PF.G", "ENB.PF.I", "ENB.PF.K", "ENB.PF.U", "ENB.PF.V", "ENB.PR.A", "ENB.PR.B", "ENB.PR.C", "ENB.PR.D", "ENB.PR.F", "ENB.PR.H", "ENB.PR.J", "ENB.PR.N", "ENB.PR.P", "ENB.PR.T", "ENB.PR.U", "ENB.PR.V", "ENB.PR.Y", "ENGH", "ENI.UN", "ENS", "ENS.PR.A", "ENT", "ENT.DB", "EOX", "EPS", "EQB", "EQB.PR.C", "EQL", "EQL.F", "EQL.U", "ER", "ERD", "ERF", "ERM", "ERO", "ESI", "ESM", "ESN", "ESP", "ET", "ETAC", "ETG", "ETHI", "ETP", "ETP.A", "ETX", "EUR", "EUR.A", "EVT", "EXE", "EXE.DB.C", "EXF", "EXN", "FAH.U", "FAI", "FAO", "FAO.U", "FAP", "FAR", "FBE", "FBU", "FC", "FC.DB.C", "FC.DB.D", "FC.DB.E", "FC.DB.F", "FC.DB.G", "FC.DB.H", "FC.DB.I", "FC.DB.J", "FCCD", "FCCL", "FCCQ", "FCID", "FCIL", "FCIQ", "FCLH", "FCQH", "FCR", "FCRH", "FCRR", "FCU", "FCUD", "FCUH", "FCUL", "FCUQ", "FDE", "FDE.A", "FDV", "FEC", "FF", "FFH", "FFH.PR.C", "FFH.PR.D", "FFH.PR.E", "FFH.PR.F", "FFH.PR.G", "FFH.PR.H", "FFH.PR.I", "FFH.PR.J", "FFH.PR.K", "FFH.PR.M", "FFH.U", "FFI.UN", "FFN", "FFN.PR.A", "FGB", "FGE", "FGE.DB.A", "FGO", "FGO.U", "FHB", "FHC", "FHC.F", "FHD", "FHE", "FHF", "FHG", "FHG.F", "FHH", "FHH.F", "FHI", "FHI.B", "FHM", "FHQ", "FHQ.F", "FHU", "FIE", "FIG", "FIG.U", "FIH.U", "FINT", "FIRE", "FIRE.DB", "FLB", "FLBA", "FLCI", "FLDM", "FLEM", "FLGA", "FLGD", "FLI", "FLOT", "FLOT.B", "FLOT.U", "FLRM", "FLSL", "FLUI", "FLUS", "FM", "FN", "FN.PR.A", "FN.PR.B", "FNV", "FOOD", "FOUR", "FPR", "FQC", "FR", "FRII", "FRL.UN", "FRU", "FRX", "FSB", "FSB.U", "FSD", "FSD.A", "FSF", "FSL", "FSL.A", "FSR", "FST", "FST.A", "FSV", "FSY", "FSZ", "FSZ.DB", "FT", "FTB", "FTG", "FTN", "FTN.PR.A", "FTS", "FTS.PR.F", "FTS.PR.G", "FTS.PR.H", "FTS.PR.I", "FTS.PR.J", "FTS.PR.K", "FTS.PR.M", "FTT", "FTU", "FTU.PR.B", "FUD", "FUD.A", "FUT", "FVI", "FVL", "FXM", "G", "GBT", "GC", "GCG", "GCG.A", "GCL", "GCL.DB.A", "GCM", "GCM.NT.U", "GCM.WT.A", "GCM.WT.B", "GCT", "GCT.C", "GDC", "GDG.UN", "GDI", "GDI.DB", "GDL", "GDV", "GDV.PR.A", "GEC.UN", "GEI", "GEI.DB", "GEN", "GEO", "GGA", "GGD", "GH", "GIB.A", "GIL", "GLG", "GMO", "GMP", "GMP.PR.B", "GMP.PR.C", "GMX", "GOGO", "GOLD", "GOOS", "GPR", "GPS", "GQM", "GQM.WT", "GRP.PR.A", "GRT.UN", "GS", "GSC", "GSV", "GSY", "GSY.DB", "GTE", "GTMS", "GUD", "GUY", "GVC", "GWO", "GWO.PR.F", "GWO.PR.G", "GWO.PR.H", "GWO.PR.I", "GWO.PR.L", "GWO.PR.M", "GWO.PR.N", "GWO.PR.O", "GWO.PR.P", "GWO.PR.Q", "GWO.PR.R", "GWO.PR.S", "GWO.PR.T", "GWR", "GXE", "GXO", "H", "HAB", "HAC", "HAD", "HAF", "HAJ", "HAL", "HARC", "HAU", "HAU.U", "HAZ", "HBAL", "HBB", "HBC", "HBD", "HBF", "HBF.U", "HBG", "HBG.U", "HBL.UN", "HBLK", "HBM", "HBP", "HBU", "HCB", "HCBB", "HCG", "HCN", "HCON", "HCRE", "HDI", "HE", "HEA", "HEA.U", "HED", "HEE", "HEF", "HEJ", "HEMB", "HEP", "HERS", "HERS.B", "HEU", "HEUR", "HEW", "HEWB", "HEX", "HEXO", "HEXO.WT", "HFA", "HFD", "HFMU", "HFMU.U", "HFP", "HFR", "HFU", "HFY", "HFY.U", "HGD", "HGGG", "HGI.UN", "HGM", "HGR", "HGU", "HGY", "HHF", "HHL", "HHL.U", "HID", "HID.B", "HIG", "HII", "HIU", "HIX", "HLC", "HLC.DB", "HLF", "HLS", "HMM.A", "HMMJ", "HMMJ.U", "HMP", "HND", "HNL", "HNU", "HNY", "HOD", "HOG", "HOM.U", "HOT.DB.U", "HOT.U", "HOT.UN", "HOU", "HPF", "HPF.U", "HPR", "HPS.A", "HQD", "HQU", "HR.UN", "HRA", "HRES", "HRR.UN", "HRT", "HRX", "HSD", "HSE", "HSE.PR.A", "HSE.PR.B", "HSE.PR.C", "HSE.PR.E", "HSE.PR.G", "HSH", "HSL", "HSM", "HSM.WT", "HSU", "HTA", "HTA.U", "HTB", "HTB.U", "HTH", "HUBL", "HUBL.U", "HUC", "HUF", "HUF.U", "HUG", "HUL", "HUL.U", "HUN", "HUTL", "HUV", "HUZ", "HWF.UN", "HWO", "HXD", "HXDM", "HXDM.U", "HXE", "HXF", "HXH", "HXQ", "HXQ.U", "HXS", "HXS.U", "HXT", "HXT.U", "HXU", "HXX", "HYD", "HYG", "HYI", "HZD", "HZM", "HZU", "IAF.PR.B", "IAF.PR.G", "IAF.PR.I", "IAG", "IAM", "IBG", "IBG.DB.D", "ICE", "ICPB", "IDG", "IDR.UN", "IEMB", "IFA", "IFB.UN", "IFC", "IFC.PR.A", "IFC.PR.C", "IFC.PR.D", "IFC.PR.E", "IFC.PR.F", "IFC.PR.G", "IFP", "IGB", "IGCF", "IGLB", "IGM", "IGM.PR.B", "III", "IIP.UN", "ILV", "ILV.F", "IMG", "IMO", "IMP", "IMV", "IN", "IN.WT", "INC.UN", "INE", "INE.DB.A", "INE.DB.B", "INE.PR.A", "INE.PR.C", "INO.UN", "INOC", "INQ", "INSR", "INV", "IPCI", "IPCO", "IPL", "IPLP", "IPO", "IQD", "IQD.B", "IRON", "ISV", "ITC", "ITH", "ITP", "ITX", "IVN", "IVQ.DB.U", "IVQ.DB.V", "IVQ.U", "JAG", "JAPN", "JAPN.B", "JE", "JE.DB.C", "JE.DB.D", "JE.PR.U", "JFS.UN", "JOY", "JWEL", "K", "KAT", "KBL", "KEG.UN", "KEL", "KEL.DB", "KER", "KEW", "KEW.WT", "KEY", "KILO", "KILO.B", "KILO.U", "KL", "KLS", "KML", "KML.PR.A", "KML.PR.C", "KMP.UN", "KOR", "KPT", "KRN", "KWH.UN", "KXS", "L", "L.PR.B", "LAC", "LAM", "LAS.A", "LB", "LB.PR.H", "LB.PR.J", "LBS", "LBS.PR.A", "LCS", "LCS.PR.A", "LDGR", "LFE", "LFE.PR.B", "LFX", "LGD", "LGD.WT", "LGO", "LGT.A", "LGT.B", "LIF", "LIFE", "LIFE.B", "LINK", "LMC", "LN", "LNF", "LNF.DB", "LNR", "LS.UN", "LUC", "LUG", "LUN", "LVN", "LVU.UN", "LXR", "LXR.WT", "LYD", "MAG", "MAL", "MAV", "MAW", "MAX", "MAXR", "MBA", "MBK.UN", "MBN", "MBX", "MCB", "MCLC", "MCSB", "MCSM", "MDF", "MDI", "MDNA", "MDS.UN", "ME", "MEE", "MEG", "MEME.B", "MEQ", "MEU", "MFC", "MFC.PR.B", "MFC.PR.C", "MFC.PR.F", "MFC.PR.G", "MFC.PR.H", "MFC.PR.I", "MFC.PR.J", "MFC.PR.K", "MFC.PR.L", "MFC.PR.M", "MFC.PR.N", "MFC.PR.O", "MFC.PR.P", "MFC.PR.Q", "MFC.PR.R", "MFI", "MFR.UN", "MFT", "MG", "MGA", "MGB", "MI.UN", "MIC", "MID.UN", "MIN", "MIND", "MINT", "MINT.B", "MIVG", "MKB", "MKC", "MKP", "MKZ.UN", "MLD.UN", "MMP.UN", "MND", "MNS", "MNS.U", "MNT", "MNT.U", "MOGO", "MOGO.DB", "MOZ", "MPC", "MPC.C", "MPCF", "MPVD", "MQR", "MR.DB", "MR.DB.A", "MR.UN", "MRC", "MRD", "MRE", "MRG.DB.A", "MRG.UN", "MRT.DB", "MRT.UN", "MRU", "MSI", "MSI.DB.A", "MSV", "MTL", "MTY", "MUB", "MULC", "MULC.B", "MUMC", "MUMC.B", "MUS", "MUSC", "MUSC.B", "MUX", "MWD", "MX", "MXF", "MXG", "MXU", "MYA", "NA", "NA.PR.A", "NA.PR.C", "NA.PR.E", "NA.PR.G", "NA.PR.S", "NA.PR.W", "NA.PR.X", "NALT", "NB", "NCF", "NCP", "NCU", "NDM", "NDM.WT.A", "NDM.WT.B", "NEO", "NEPT", "NEW.A", "NEW.PR.D", "NEXA", "NEXT", "NFAM", "NFI", "NG", "NGD", "NGI.UN", "NGQ", "NHK", "NIF.UN", "NKO", "NKO.NT", "NML", "NMX", "NMX.WT", "NOA", "NOA.DB", "NPF.UN", "NPI", "NPI.DB.C", "NPI.PR.A", "NPI.PR.B", "NPI.PR.C", "NPK", "NPRF", "NREA", "NRI", "NSU", "NTR", "NUS", "NVA", "NVCN", "NVU.DB", "NVU.UN", "NWC", "NWH.DB", "NWH.DB.C", "NWH.DB.D", "NWH.DB.E", "NWH.DB.F", "NWH.DB.G", "NWH.UN", "NXE", "NXF", "NXF.B", "NXJ", "NZC", "OBE", "OCS.UN", "OGC", "OGD", "OLA", "OLY", "OMI", "ONC", "ONC.WT", "ONEB", "ONEQ", "ONEX", "OPS", "OPT", "OR", "OR.DB", "OR.WT", "OR.WT.A", "ORA", "ORL", "ORV", "OSB", "OSK", "OSL.UN", "OSP", "OSP.PR.A", "OTEX", "OXC", "PAAS", "PAR.UN", "PATH", "PAY", "PBD", "PBH", "PBH.DB.E", "PBH.DB.F", "PBH.DB.G", "PBI", "PBI.B", "PBL", "PBY.UN", "PCD.UN", "PCY", "PD", "PDC", "PDF", "PDIV", "PDL", "PDV", "PDV.PR.A", "PEGI", "PEU", "PEU.B", "PEY", "PFB", "PFG", "PFH.F", "PFL", "PFT.UN", "PG", "PGF", "PGI.UN", "PGLC", "PHE", "PHE.B", "PHO", "PHR", "PHW", "PHX", "PHYS", "PHYS.U", "PIC.A", "PIC.PR.A", "PID", "PIF", "PIN", "PINC", "PINV", "PKI", "PL", "PLC", "PLDI", "PLI", "PLV", "PLZ.DB.E", "PLZ.UN", "PMB.UN", "PME", "PMIF", "PMIF.U", "PMM", "PMN", "PMNT", "PMT", "PMTS", "PNC.A", "PNC.B", "PNE", "PNP", "POM", "PONY", "POU", "POW", "POW.PR.A", "POW.PR.B", "POW.PR.C", "POW.PR.D", "POW.PR.E", "POW.PR.F", "POW.PR.G", "PPL", "PPL.PF.A", "PPL.PR.A", "PPL.PR.C", "PPL.PR.E", "PPL.PR.G", "PPL.PR.I", "PPL.PR.K", "PPL.PR.M", "PPL.PR.O", "PPL.PR.Q", "PPL.PR.S", "PPR", "PPR.WT", "PPS", "PR", "PRA", "PRM", "PRM.PR.A", "PRN", "PRP", "PRQ", "PRU", "PSA", "PSB", "PSD", "PSI", "PSK", "PSLV", "PSLV.U", "PSU.U", "PSY", "PSY.U", "PTB", "PTG", "PTM", "PTM.WT.U", "PTS", "PUD", "PUD.B", "PVG", "PVS.PR.D", "PVS.PR.E", "PVS.PR.F", "PVS.PR.G", "PWF", "PWF.PR.A", "PWF.PR.E", "PWF.PR.F", "PWF.PR.G", "PWF.PR.H", "PWF.PR.I", "PWF.PR.K", "PWF.PR.L", "PWF.PR.O", "PWF.PR.P", "PWF.PR.Q", "PWF.PR.R", "PWF.PR.S", "PWF.PR.T", "PWF.PR.Z", "PXC", "PXG", "PXG.U", "PXS", "PXS.U", "PXT", "PXU.F", "PYF", "PYF.B", "PYF.U", "PZA", "PZC", "PZW", "PZW.F", "PZW.U", "QAH", "QBB", "QBR.A", "QBR.B", "QCD", "QCE", "QCN", "QDX", "QDXH", "QEC", "QEM", "QGL", "QHY", "QIE", "QMA", "QMY", "QQC.F", "QSB", "QSP.UN", "QSR", "QTRH", "QUIG", "QUS", "QUU", "QXM", "RAI.UN", "RAV.UN", "RAY.A", "RAY.B", "RBA", "RBDI", "RBN.UN", "RBNK", "RBO", "RBOT", "RBOT.U", "RCD", "RCE", "RCH", "RCI.A", "RCI.B", "RCO.UN", "RDL", "REAL", "RECP", "REI.UN", "REIT", "RET", "RET.A", "RFP", "RGRE", "RGRE.U", "RGX", "RIB.UN", "RID", "RID.U", "RIDH", "RIE", "RIE.U", "RIEH", "RIG", "RIG.U", "RIT", "RLB", "RLD", "RLE", "RMBO", "RME", "RMX", "RNW", "RNX", "ROOT", "ROXG", "RPD", "RPD.U", "RPDH", "RPF", "RPI.UN", "RPSB", "RQG", "RQH", "RQI", "RQJ", "RQK", "RQL", "RQN", "RSI", "RSI.DB.E", "RSI.DB.F", "RTG", "RUBH", "RUBY", "RUBY.U", "RUD", "RUD.U", "RUDH", "RUE", "RUE.U", "RUEH", "RUS", "RUSB", "RUSB.U", "RVX", "RVX.WT", "RWC", "RWE", "RWE.B", "RWU", "RWU.B", "RWW", "RWW.B", "RWX", "RWX.B", "RXD", "RXD.U", "RXE", "RXE.U", "RY", "RY.PR.A", "RY.PR.C", "RY.PR.E", "RY.PR.F", "RY.PR.G", "RY.PR.H", "RY.PR.I", "RY.PR.J", "RY.PR.K", "RY.PR.L", "RY.PR.M", "RY.PR.N", "RY.PR.O", "RY.PR.P", "RY.PR.Q", "RY.PR.R", "RY.PR.S", "RY.PR.W", "RY.PR.Z", "S", "S.WT", "SAM", "SAP", "SAU", "SBB", "SBC", "SBC.PR.A", "SBI", "SBN", "SBN.PR.A", "SBND", "SBR", "SBT", "SBT.B", "SBT.U", "SCAD", "SCB", "SCL", "SCU", "SCY", "SDY", "SEA", "SEC", "SEED", "SES", "SEV", "SEV.DB.A", "SFD", "SFIX", "SGY", "SGY.DB", "SHC", "SHE", "SHLE", "SHOP", "SHZ", "SIA", "SID", "SII", "SINT", "SIS", "SJ", "SJR.B", "SJR.PR.A", "SJR.PR.B", "SKG.UN", "SLF", "SLF.PR.A", "SLF.PR.B", "SLF.PR.C", "SLF.PR.D", "SLF.PR.E", "SLF.PR.G", "SLF.PR.H", "SLF.PR.I", "SLF.PR.J", "SLF.PR.K", "SLR", "SMC", "SMF", "SMT", "SMU.UN", "SNC", "SOLG", "SOP", "SOT.DB", "SOT.UN", "SOX", "SOX.DB.A", "SOY", "SPB", "SPG", "SPG.WT", "SPPP", "SPPP.U", "SQP", "SRHI", "SRHI.WT", "SRT.U", "SRT.UN", "SRU.UN", "SRV.UN", "SRX", "SSF.UN", "SSL", "SSL.WT", "SSRM", "STEP", "STGO", "STLC", "STN", "STPL", "SU", "SUM", "SUSA", "SVB", "SVM", "SVR", "SVR.C", "SW", "SWH", "SWP", "SWY", "SWY.DB.U", "SXI", "SXP", "SYLD", "T", "TA", "TA.PR.D", "TA.PR.E", "TA.PR.F", "TA.PR.H", "TA.PR.J", "TAO", "TAO.WT", "TBL", "TC", "TCL.A", "TCL.B", "TCN", "TCN.DB.U", "TCS", "TCSB", "TCT.UN", "TCW", "TD", "TD.PF.A", "TD.PF.B", "TD.PF.C", "TD.PF.D", "TD.PF.E", "TD.PF.F", "TD.PF.G", "TD.PF.H", "TD.PF.I", "TD.PF.J", "TD.PF.K", "TD.PF.L", "TDB", "TDG", "TECK.A", "TECK.B", "TEI", "TEI.DB", "TEL", "TEV", "TEV.WT", "TF", "TF.DB.A", "TF.DB.B", "TF.DB.C", "TFII", "TGL", "TGO", "TGOD", "TGOD.WT", "TGZ", "TH", "TH.DB.U", "THE", "THNK", "THO", "THU", "TI", "TIH", "TIME", "TIME.B", "TKO", "TLF", "TLG", "TLO", "TLV", "TMD", "TMD.WT.F", "TMD.WT.G", "TMD.WT.H", "TMD.WT.I", "TMI", "TMI.B", "TML", "TMQ", "TMR", "TNP", "TNT.UN", "TNX", "TOG", "TOS", "TOT", "TOU", "TOY", "TPE", "TPH", "TPH.DB.E", "TPRF", "TPU", "TPX.A", "TPX.B", "TRI", "TRI.PR.B", "TRIL", "TRL", "TRL.WT", "TRP", "TRP.PR.A", "TRP.PR.B", "TRP.PR.C", "TRP.PR.D", "TRP.PR.E", "TRP.PR.F", "TRP.PR.G", "TRP.PR.H", "TRP.PR.I", "TRP.PR.J", "TRP.PR.K", "TRQ", "TRST", "TRZ", "TS.B", "TSGI", "TSL", "TSU", "TTP", "TUSB", "TUSB.U", "TUT.UN", "TV", "TVA.B", "TVE", "TVK", "TVK.DB", "TWC", "TWM", "TXF", "TXF.B", "TXG", "TXP", "TXT.PR.A", "TXT.UN", "TZS", "TZZ", "U", "UEX", "UFS", "ULV.C", "ULV.F", "ULV.U", "UMI", "UMI.B", "UNC", "UNC.PR.A", "UNC.PR.B", "UNC.PR.C", "UNI", "UNS", "UR", "URB", "URB.A", "URE", "USA", "USB", "USB.U", "USF.UN", "UTE.UN", "UWE", "UXM", "UXM.B", "VA", "VAB", "VAH", "VB", "VB.PR.A", "VB.PR.B", "VBAL", "VBG", "VBU", "VCB", "VCE", "VCIP", "VCM", "VCN", "VCNS", "VDU", "VDY", "VE", "VEE", "VEF", "VEH", "VEQT", "VET", "VFF", "VFV", "VGG", "VGH", "VGRO", "VGV", "VGZ", "VI", "VIDY", "VII", "VIU", "VLB", "VLE", "VLN", "VLQ", "VMD", "VMO", "VNP", "VNP.DB", "VNR", "VNR.PR.A", "VRE", "VSB", "VSC", "VSG", "VSP", "VUN", "VUS", "VVL", "VVO", "VXC", "VXM", "VXM.B", "W.PR.H", "W.PR.J", "W.PR.K", "W.PR.M", "WCM.A", "WCM.B", "WCN", "WCP", "WDO", "WEED", "WEF", "WFC", "WFS", "WFS.PR.A", "WFT", "WIR.U", "WJA", "WJX", "WM", "WN", "WN.PR.A", "WN.PR.C", "WN.PR.D", "WN.PR.E", "WOMN", "WPK", "WPM", "WPRT", "WRG", "WRN", "WRX", "WSP", "WTE", "WXM", "X", "XAM", "XAU", "XAW", "XBAL", "XBB", "XBM", "XCB", "XCD", "XCG", "XCH", "XCS", "XCT", "XCV", "XDG", "XDGH", "XDIV", "XDU", "XDUH", "XDV", "XEB", "XEC", "XEF", "XEG", "XEH", "XEI", "XEM", "XEN", "XEU", "XFA", "XFC", "XFF", "XFH", "XFI", "XFN", "XFR", "XFS", "XGB", "XGD", "XGI", "XGRO", "XHB", "XHC", "XHD", "XHU", "XHY", "XIC", "XID", "XIG", "XIN", "XIT", "XIU", "XLB", "XMA", "XMC", "XMD", "XMF.A", "XMF.PR.B", "XMF.PR.C", "XMH", "XMI", "XML", "XMM", "XMS", "XMU", "XMV", "XMW", "XMY", "XPF", "XQB", "XQQ", "XRB", "XRE", "XSB", "XSC", "XSE", "XSH", "XSI", "XSP", "XSQ", "XST", "XSU", "XTC", "XTD", "XTD.PR.A", "XTG", "XTR", "XUH", "XUS", "XUT", "XUU", "XWD", "XXM", "XXM.B", "Y", "Y.WT", "YCM", "YCM.PR.A", "YCM.PR.B", "YGR", "YPG.DB", "YRB", "YRI", "YXM", "YXM.B", "ZAG", "ZAR", "ZBAL", "ZBK", "ZCB", "ZCH", "ZCL", "ZCM", "ZCN", "ZCON", "ZCPB", "ZCS", "ZCS.L", "ZDB", "ZDH", "ZDI", "ZDJ", "ZDM", "ZDV", "ZDY", "ZDY.U", "ZEA", "ZEB", "ZEF", "ZEM", "ZEO", "ZEQ", "ZEUS", "ZFC", "ZFH", "ZFL", "ZFM", "ZFN", "ZFS", "ZFS.L", "ZGB", "ZGD", "ZGI", "ZGQ", "ZGRO", "ZGSB", "ZHP", "ZHU", "ZHY", "ZIC", "ZIC.U", "ZID", "ZIN", "ZJG", "ZJK", "ZJN", "ZJO", "ZLB", "ZLC", "ZLD", "ZLE", "ZLH", "ZLI", "ZLU", "ZLU.U", "ZMI", "ZMP", "ZMSB", "ZMT", "ZMU", "ZNQ", "ZPH", "ZPL", "ZPR", "ZPS", "ZPS.L", "ZPW", "ZPW.U", "ZQQ", "ZRE", "ZRR", "ZSB", "ZSP", "ZSP.U", "ZST", "ZST.L", "ZSU", "ZUB", "ZUD", "ZUE", "ZUH", "ZUP", "ZUP.U", "ZUQ", "ZUS.U", "ZUS.V", "ZUT", "ZVC", "ZVI", "ZVU", "ZWA", "ZWB", "ZWC", "ZWE", "ZWH", "ZWH.U", "ZWK", "ZWP", "ZWS", "ZWU", "ZXM", "ZXM.B", "ZYME", "ZZZ", "ZZZD"]
url = "https://web.tmxmoney.com/quote.php?qm_symbol=BBD.A"
page = requests.get(url)
#while loop to get the data from all 2274 symbols
##i = 0
##while i < len(Symbol):
##    print(Symbol[i]+"\t"+str(i))
##    i =i+ 1

# parse webpage with BeautifulSoup, get tags with class "detailed-quote-table'
soup = BeautifulSoup(page.text, "html.parser")
detailed_quote_tables = soup.findAll(class_="detailed-quote-table")

# clean data into list format
detailed_quotes_text_list = [dq.get_text() for dq in detailed_quote_tables]
detailed_quotes_string = ''.join(detailed_quotes_text_list)
detailed_quotes = detailed_quotes_string.split('\n\n')

# remove empty element
for dq in detailed_quotes:
    if dq == '':
        detailed_quotes.remove(dq)

# clean data for csv format, like change line-break to comman etc
# this part is slow (because of string creation) so should find a better way
for i in range(len(detailed_quotes)):
    detailed_quotes[i] = detailed_quotes[i].replace('Prev. Close:', 'Prev. Close:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('Dividend:', 'Dividend:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('Yield:', 'Yield:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('Exchange:', 'Exchange:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('\t', '')
    detailed_quotes[i] = detailed_quotes[i].replace('\n', ',')
    if i > 0:
        detailed_quotes[i] = detailed_quotes[i].replace(',', '', 1)
        
#trying to remove commas in a certain range
##str = detailed_quotes
##print(str)
##start = str.find("Diluted Avg Shares (Last Qtr):") + 31
##end = detailed_quotes.find("Prev. Close:Pr")
##str = str[0:start] + str[start:end].replace(',', '') + str[end:]

#check 
i = 0
while i < 100:
    print(detailed_quotes[i]+"\n")
    i =i+ 1
        
# write data to file
with open("C:\\Users\\kevin\\Desktop\\python file exsports\\soup.csv", "w") as f:           #"w" for write and "a" for append
    f.write('\n'.join(detailed_quotes))
    #f.write('\n'.join(detailed_quotes))

#Transpose data
#attempt 1
#pd.read_csv('soup.csv', header=None).T.to_csv('soup.csv_output.csv', header=False, index=False)
#Attempt 2
#a = izip(*csv.reader(open("soup.csv", "rb")))
#csv.writer(open("soup.csv_output.csv", "wb")).writerows(a)


    
print(detailed_quotes)
