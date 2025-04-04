export interface IProvider {
  id: number
  registro_ans?: string
  cnpj?: string
  razao_social?: string
  nome_fantasia?: string
  modalidade?: string
  logradouro?: string
  numero?: string
  complemento?: string
  bairro?: string
  cidade?: string
  uf?: string
  cep?: string
  ddd?: string
  telefone?: string
  fax?: string
  endereco_eletronico?: string
  representante?: string
  cargo_representante?: string
  regiao_de_comercializacao?: number
  data_registro_ans: string
}
