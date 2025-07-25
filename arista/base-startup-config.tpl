// Copyright 2020 Nokia
// Licensed under the BSD 3-Clause License.
// SPDX-License-Identifier: BSD-3-Clause
// Original file: https://github.com/srl-labs/containerlab/blob/main/nodes/ceos/ceos.cfg

hostname {{ .ShortName }}
username admin privilege 15 secret admin
!
aaa authorization exec default local
!
service routing protocols model multi-agent
!
{{- if .Env.CLAB_MGMT_VRF }}
vrf instance {{ .Env.CLAB_MGMT_VRF }}
!
{{end}}
{{ if .MgmtIPv4Gateway }}ip route {{ if .Env.CLAB_MGMT_VRF }}vrf {{ .Env.CLAB_MGMT_VRF }} {{end}}0.0.0.0/0 {{ .MgmtIPv4Gateway }}{{end}}
{{ if .MgmtIPv6Gateway }}ipv6 route {{ if .Env.CLAB_MGMT_VRF }}vrf {{ .Env.CLAB_MGMT_VRF }} {{end}}::0/0 {{ .MgmtIPv6Gateway }}{{end}}
!
interface {{ .MgmtIntf }}
{{ if .Env.CLAB_MGMT_VRF }} vrf {{ .Env.CLAB_MGMT_VRF }}{{end}}
{{ if .MgmtIPv4Address }}ip address {{ .MgmtIPv4Address }}/{{.MgmtIPv4PrefixLength}}{{end}}
{{ if .MgmtIPv6Address }}ipv6 address {{ .MgmtIPv6Address }}/{{.MgmtIPv6PrefixLength}}{{end}}
no lldp transmit
no lldp receive
!
management api gnmi
   transport grpc default
{{ if .Env.CLAB_MGMT_VRF }}      vrf {{ .Env.CLAB_MGMT_VRF }}{{end}}
!
management api netconf
   transport ssh default
{{ if .Env.CLAB_MGMT_VRF }}      vrf {{ .Env.CLAB_MGMT_VRF }}{{end}}
!
management api http-commands
   no shutdown
{{- if .Env.CLAB_MGMT_VRF }}
   !
   vrf {{ .Env.CLAB_MGMT_VRF }}
      no shutdown
{{end}}
!
end

