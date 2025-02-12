#!/usr/bin/env python

registers = {
0x0000 : 'REG_SYS_ISO_CTRL_8703B',
0x0002 : 'REG_SYS_FUNC_EN_8703B',
0x0004 : 'REG_APS_FSMCO_8703B',
0x0008 : 'REG_SYS_CLKR_8703B',
0x000A : 'REG_9346CR_8703B',
0x000C : 'REG_EE_VPD_8703B',
0x0010 : 'REG_AFE_MISC_8703B',
0x0011 : 'REG_SPS0_CTRL_8703B',
0x0018 : 'REG_SPS_OCP_CFG_8703B',
0x001C : 'REG_RSV_CTRL_8703B',
0x001F : 'REG_RF_CTRL_8703B',
0x0023 : 'REG_LPLDO_CTRL_8703B',
0x0024 : 'REG_AFE_XTAL_CTRL_8703B',
0x0028 : 'REG_AFE_PLL_CTRL_8703B',
0x002c : 'REG_MAC_PLL_CTRL_EXT_8703B',
0x0030 : 'REG_EFUSE_CTRL_8703B',
0x0034 : 'REG_EFUSE_TEST_8703B',
0x0038 : 'REG_PWR_DATA_8703B',
0x003C : 'REG_CAL_TIMER_8703B',
0x003E : 'REG_ACLK_MON_8703B',
0x0040 : 'REG_GPIO_MUXCFG_8703B',
0x0042 : 'REG_GPIO_IO_SEL_8703B',
0x0043 : 'REG_MAC_PINMUX_CFG_8703B',
0x0044 : 'REG_GPIO_PIN_CTRL_8703B',
0x0048 : 'REG_GPIO_INTM_8703B',
0x004C : 'REG_LEDCFG0_8703B',
0x004D : 'REG_LEDCFG1_8703B',
0x004E : 'REG_LEDCFG2_8703B',
0x004F : 'REG_LEDCFG3_8703B',
0x0050 : 'REG_FSIMR_8703B',
0x0054 : 'REG_FSISR_8703B',
0x0058 : 'REG_HSIMR_8703B',
0x005c : 'REG_HSISR_8703B',
0x0060 : 'REG_GPIO_EXT_CTRL',
0x0064 : 'REG_PAD_CTRL1_8703B',
0x0068 : 'REG_MULTI_FUNC_CTRL_8703B',
0x006C : 'REG_GPIO_STATUS_8703B',
0x0070 : 'REG_SDIO_CTRL_8703B',
0x0074 : 'REG_OPT_CTRL_8703B',
0x0078 : 'REG_AFE_CTRL_4_8703B',
0x007C : 'REG_LDO_SWR_CTRL',
0x0080 : 'REG_MCUFWDL_8703B',
0x0088 : 'REG_HMEBOX_DBG_0_8703B',
0x008A : 'REG_HMEBOX_DBG_1_8703B',
0x008C : 'REG_HMEBOX_DBG_2_8703B',
0x008E : 'REG_HMEBOX_DBG_3_8703B',
0x00B0 : 'REG_HIMR0_8703B',
0x00B4 : 'REG_HISR0_8703B',
0x00B8 : 'REG_HIMR1_8703B',
0x00BC : 'REG_HISR1_8703B',
0x00CC : 'REG_PMC_DBG_CTRL2_8703B',
0x00CF : 'REG_EFUSE_BURN_GNT_8703B',
0x00EC : 'REG_HPON_FSM_8703B',
0x00F0 : 'REG_SYS_CFG_8703B',
0x00F4 : 'REG_SYS_STATUS1',
0x00F8 : 'REG_SYS_STATUS2',
0x00FC : 'REG_SYS_CFG1_8703B',
0x00FD : 'REG_ROM_VERSION',
0x0100 : 'REG_CR',
0x0114 : 'REG_TRXFF_BNDY',
0x0130 : 'REG_FWIMR',
0x01A0 : 'REG_C2HEVT_CMD_ID_8703B',
0x01A1 : 'REG_C2HEVT_CMD_SEQ_88XX',
0x01A2 : 'REG_C2hEVT_CMD_CONTENT_88XX',
0x01AE : 'REG_C2HEVT_CMD_LEN_8703B',
0x01AF : 'REG_C2HEVT_CLEAR_8703B',
0x01C0 : 'REG_MCUTST_1_8703B',
0x01C7 : 'REG_WOWLAN_WAKE_REASON',
0x01C8 : 'REG_FMETHR_8703B',
0x01CC : 'REG_HMETFR_8703B',
0x01D0 : 'REG_HMEBOX_0_8703B',
0x01D4 : 'REG_HMEBOX_1_8703B',
0x01D8 : 'REG_HMEBOX_2_8703B',
0x01DC : 'REG_HMEBOX_3_8703B',
0x01E0 : 'REG_LLT_INIT_8703B',
0x01F0 : 'REG_HMEBOX_EXT0_8703B',
0x01F4 : 'REG_HMEBOX_EXT1_8703B',
0x01F8 : 'REG_HMEBOX_EXT2_8703B',
0x01FC : 'REG_HMEBOX_EXT3_8703B',
0x0200 : 'REG_RQPN_8703B',
0x0204 : 'REG_FIFOPAGE_8703B',
0x0208 : 'REG_DWBCN0_CTRL_8703B',
0x020c : 'REG_TXDMA_OFFSET_CHK_8703B',
0x0210 : 'REG_TXDMA_STATUS_8703B',
0x0214 : 'REG_RQPN_NPQ_8703B',
0x0228 : 'REG_DWBCN1_CTRL_8703B',
0x0280 : 'REG_RXDMA_AGG_PG_TH_8703B',
0x0284 : 'REG_FW_UPD_RDPTR_8703B',
0x0286 : 'REG_RXDMA_CONTROL_8703B',
0x0287 : 'REG_RXPKT_NUM_8703B',
0x0288 : 'REG_RXDMA_STATUS_8703B',
0x0290 : 'REG_RXDMA_MODE_CTRL_8703B',
0x02BC : 'REG_EARLY_MODE_CONTROL_8703B',
0x02F0 : 'REG_RSVD5_8703B',
0x02F4 : 'REG_RSVD6_8703B',
0x0300 : 'REG_PCIE_CTRL_REG_8703B',
0x0304 : 'REG_INT_MIG_8703B',
0x0308 : 'REG_BCNQ_DESA_8703B',
0x0310 : 'REG_HQ_DESA_8703B',
0x0318 : 'REG_MGQ_DESA_8703B',
0x0320 : 'REG_VOQ_DESA_8703B',
0x0328 : 'REG_VIQ_DESA_8703B',
0x0330 : 'REG_BEQ_DESA_8703B',
0x0338 : 'REG_BKQ_DESA_8703B',
0x0340 : 'REG_RX_DESA_8703B',
0x0348 : 'REG_DBI_WDATA_8703B',
0x034C : 'REG_DBI_RDATA_8703B',
0x0350 : 'REG_DBI_ADDR_8703B',
0x0352 : 'REG_DBI_FLAG_8703B',
0x0354 : 'REG_MDIO_WDATA_8703B',
0x0356 : 'REG_MDIO_RDATA_8703B',
0x0358 : 'REG_MDIO_CTL_8703B',
0x0360 : 'REG_DBG_SEL_8703B',
0x0361 : 'REG_PCIE_HRPWM_8703B',
0x0363 : 'REG_PCIE_HCPWM_8703B',
0x036A : 'REG_PCIE_MULTIFET_CTRL_8703B',
0x0400 : 'REG_VOQ_INFORMATION_8703B',
0x0404 : 'REG_VIQ_INFORMATION_8703B',
0x0408 : 'REG_BEQ_INFORMATION_8703B',
0x040C : 'REG_BKQ_INFORMATION_8703B',
0x0410 : 'REG_MGQ_INFORMATION_8703B',
0x0414 : 'REG_HGQ_INFORMATION_8703B',
0x0418 : 'REG_BCNQ_INFORMATION_8703B',
0x041A : 'REG_TXPKT_EMPTY_8703B',
0x0420 : 'REG_FWHW_TXQ_CTRL_8703B',
0x0423 : 'REG_HWSEQ_CTRL_8703B',
0x0424 : 'REG_TXPKTBUF_BCNQ_BDNY_8703B',
0x0425 : 'REG_TXPKTBUF_MGQ_BDNY_8703B',
0x0426 : 'REG_LIFECTRL_CTRL_8703B',
0x0427 : 'REG_MULTI_BCNQ_OFFSET_8703B',
0x0428 : 'REG_SPEC_SIFS_8703B',
0x042A : 'REG_RL_8703B',
0x042C : 'REG_TXBF_CTRL_8703B',
0x0430 : 'REG_DARFRC_8703B',
0x0434 : 'REG_DARFRC_8703B_H',
0x0438 : 'REG_RARFRC_8703B',
0x043C : 'REG_RARFRC_8703B_H',
0x0440 : 'REG_RRSR_8703B',
0x0444 : 'REG_ARFR0_8703B',
0x0448 : 'REG_ARFR0_8703B_H',
0x044C : 'REG_ARFR1_8703B',
0x0450 : 'REG_ARFR1_8703B_H',
0x0454 : 'REG_CCK_CHECK_8703B',
0x0456 : 'REG_AMPDU_MAX_TIME_8703B',
0x0457 : 'REG_TXPKTBUF_BCNQ_BDNY1_8703B',
0x0458 : 'REG_AMPDU_MAX_LENGTH_8703B',
0x045D : 'REG_TXPKTBUF_WMAC_LBK_BF_HD_8703B',
0x045F : 'REG_NDPA_OPT_CTRL_8703B',
0x0460 : 'REG_FAST_EDCA_CTRL_8703B',
0x0463 : 'REG_RD_RESP_PKT_TH_8703B',
0x0483 : 'REG_DATA_SC_8703B',
0x0484 : 'REG_TXPKTBUF_IV_LOW',
0x0488 : 'REG_TXPKTBUF_IV_HIGH',
0x04AC : 'REG_TXRPT_START_OFFSET',
0x04B4 : 'REG_POWER_STAGE1_8703B',
0x04B8 : 'REG_POWER_STAGE2_8703B',
0x04BC : 'REG_AMPDU_BURST_MODE_8703B',
0x04C0 : 'REG_PKT_VO_VI_LIFE_TIME_8703B',
0x04C2 : 'REG_PKT_BE_BK_LIFE_TIME_8703B',
0x04C4 : 'REG_STBC_SETTING_8703B',
0x04C7 : 'REG_HT_SINGLE_AMPDU_8703B',
0x04C8 : 'REG_PROT_MODE_CTRL_8703B',
0x04CA : 'REG_MAX_AGGR_NUM_8703B',
0x04CB : 'REG_RTS_MAX_AGGR_NUM_8703B',
0x04CC : 'REG_BAR_MODE_CTRL_8703B',
0x04CF : 'REG_RA_TRY_RATE_AGG_LMT_8703B',
0x04D0 : 'REG_MACID_PKT_DROP0_8703B',
0x04D4 : 'REG_MACID_PKT_SLEEP_8703B',
0x0500 : 'REG_EDCA_VO_PARAM_8703B',
0x0504 : 'REG_EDCA_VI_PARAM_8703B',
0x0508 : 'REG_EDCA_BE_PARAM_8703B',
0x050C : 'REG_EDCA_BK_PARAM_8703B',
0x0510 : 'REG_BCNTCFG_8703B',
0x0512 : 'REG_PIFS_8703B',
0x0513 : 'REG_RDG_PIFS_8703B',
0x0514 : 'REG_SIFS_CTX_8703B',
0x0516 : 'REG_SIFS_TRX_8703B',
0x051A : 'REG_AGGR_BREAK_TIME_8703B',
0x051B : 'REG_SLOT_8703B',
0x0520 : 'REG_TX_PTCL_CTRL_8703B',
0x0522 : 'REG_TXPAUSE_8703B',
0x0523 : 'REG_DIS_TXREQ_CLR_8703B',
0x0524 : 'REG_RD_CTRL_8703B',
0x0540 : 'REG_TBTT_PROHIBIT_8703B',
0x0544 : 'REG_RD_NAV_NXT_8703B',
0x0546 : 'REG_NAV_PROT_LEN_8703B',
0x0550 : 'REG_BCN_CTRL_8703B',
0x0551 : 'REG_BCN_CTRL_CLINT0',
0x0552 : 'REG_MBID_NUM_8703B',
0x0553 : 'REG_DUAL_TSF_RST_8703B',
0x0554 : 'REG_BCN_INTERVAL_8703B',
0x0558 : 'REG_DRVERLYINT_8703B',
0x0559 : 'REG_BCNDMATIM_8703B',
0x055A : 'REG_ATIMWND_8703B',
0x055C : 'REG_USTIME_TSF_8703B',
0x055D : 'REG_BCN_MAX_ERR_8703B',
0x055E : 'REG_RXTSF_OFFSET_CCK_8703B',
0x055F : 'REG_RXTSF_OFFSET_OFDM_8703B',
0x0560 : 'REG_TSFTR_8703B',
0x0572 : 'REG_CTWND_8703B',
0x0577 : 'REG_SECONDARY_CCA_CTRL_8703B',
0x0580 : 'REG_PSTIMER_8703B',
0x0584 : 'REG_TIMER0_8703B',
0x0588 : 'REG_TIMER1_8703B',
0x05C0 : 'REG_ACMHWCTRL_8703B',
0x05F8 : 'REG_SCH_TXCMD_8703B',
0x0600 : 'REG_MAC_CR_8703B',
0x0604 : 'REG_TCR_8703B',
0x0608 : 'REG_RCR_8703B',
0x060C : 'REG_RX_PKT_LIMIT_8703B',
0x060D : 'REG_RX_DLK_TIME_8703B',
0x060F : 'REG_RX_DRVINFO_SZ_8703B',
0x0610 : 'REG_MACID_8703B',
0x0618 : 'REG_BSSID_8703B',
0x0620 : 'REG_MAR_8703B',
0x0624 : 'REG_MAR_8703B_H',
0x0628 : 'REG_MBIDCAMCFG_8703B',
0x0630 : 'REG_WOWLAN_GTK_DBG1',
0x0634 : 'REG_WOWLAN_GTK_DBG2',
0x0638 : 'REG_USTIME_EDCA_8703B',
0x063A : 'REG_MAC_SPEC_SIFS_8703B',
0x063C : 'REG_RESP_SIFP_CCK_8703B',
0x063E : 'REG_RESP_SIFS_OFDM_8703B',
0x0640 : 'REG_ACKTO_8703B',
0x0641 : 'REG_CTS2TO_8703B',
0x0642 : 'REG_EIFS_8703B',
0x0652 : 'REG_NAV_UPPER_8703B',
0x0668 : 'REG_TRXPTCL_CTL_8703B',
0x066C : 'REG_TRXPTCL_CTL_8703B_H',
0x0670 : 'REG_CAMCMD_8703B',
0x0674 : 'REG_CAMWRITE_8703B',
0x0678 : 'REG_CAMREAD_8703B',
0x067C : 'REG_CAMDBG_8703B',
0x0680 : 'REG_SECCFG_8703B',
0x0690 : 'REG_WOW_CTRL_8703B',
0x0692 : 'REG_PS_RX_INFO_8703B',
0x0693 : 'REG_UAPSD_TID_8703B',
0x0698 : 'REG_WKFMCAM_CMD_8703B',
0x0698 : 'REG_WKFMCAM_NUM_8703B',
0x069C : 'REG_WKFMCAM_RWD_8703B',
0x06A0 : 'REG_RXFLTMAP0_8703B',
0x06A2 : 'REG_RXFLTMAP1_8703B',
0x06A4 : 'REG_RXFLTMAP2_8703B',
0x06A8 : 'REG_BCN_PSR_RPT_8703B',
0x06C0 : 'REG_BT_COEX_TABLE_8703B_0',
0x06C4 : 'REG_BT_COEX_TABLE_8703B_1',
0x06C8 : 'REG_BT_COEX_BRK_TABLE',
0x06CC : 'REG_BT_COEX_TABLE_H',
0x06E4 : 'REG_BFMER0_INFO_8703B',
0x06EC : 'REG_BFMER1_INFO_8703B',
0x06F4 : 'REG_CSI_RPT_PARAM_BW20_8703B',
0x06F8 : 'REG_CSI_RPT_PARAM_BW40_8703B',
0x06FC : 'REG_CSI_RPT_PARAM_BW80_8703B',
0x0700 : 'REG_MACID1_8703B',
0x0708 : 'REG_BSSID1_8703B',
0x0714 : 'REG_BFMEE_SEL_8703B',
0x0718 : 'REG_SND_PTCL_CTRL_8703B',
0x0765 : 'REG_GNT_BT',
0x076E : 'REG_BT_COEX_ENH_INTR_CTRL',
0x0778 : 'REG_BT_STAT_CTRL',
0x0790 : 'REG_BT_TDMA_TIME',
0x07C0 : 'REG_LTECOEX_CTRL',
0x07C4 : 'REG_LTECOEX_WRITE_DATA',
0x07C8 : 'REG_LTECOEX_READ_DATA',
0x0070 : 'REG_LTECOEX_PATH_CONTROL',
0x0C78 : 'REG_AGCRSSI',
}
