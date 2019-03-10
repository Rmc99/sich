/*
não está sendo usado
$(document).ready(function() {
    $("#id_categoria, #id_qtd_horas, #id_valor_hora, #id_qtd_dependente_irpf, #id_valor_pensao").on('keyup change', function() {
        var vbruto = parseFloat($('#id_valor_bruto').val());
        var qhora = parseInt($('#id_qtd_horas').val());
        var vhora = parseFloat($('#id_valor_pensao').val());
        //var qdep = parseInt($('#id_qtd_dependente_irpf').val()) || 0;
        var qdep = parseInt($('#id_qtd_dependente_irpf').val());
        var cteg = $("#id_categoria option:selected").val();
        var vpensao = parseFloat($('#id_valor_pensao').val());

        // calculo valor bruto
        var vbruto = qhora * vhora;
        // calculo iss 5%
        var iss = vbruto * 0.05;

        // calculo inss 11%
        var inss = vbruto * 0.11;

        // calculo para valor base para saber aliquota
        var vbase = vbruto - inss;

        // calculo patronal 20%
        var ptnal = vbruto * 0.20;

        // calculo deducao irpf
        var dirpf = inss+(qdep*189.59);

        // calculo pos deducao irpf
        var pos_irpf = vbruto-inss;

// Calculos para Colaborador/Professor Interno do IFMA e COLUN
        if (cteg == 1 || cteg == 3) {
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(0);
            $('#id_valor_iss').val(0);
            $('#id_deducao_irpf').val(0);
            $('#id_valor_pos_deducao_irpf').val(0);
            $('#id_valor_irpf').val(0);
            $('#id_valor_patronal').val(ptnal);
            $('#id_valor_liquido').val(vbruto);
        }
// Calculos para Colaborador/Professor Externo
        else if (vbase <= 1903.98){
            var irpf = 0;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            var vliq = vbruto-inss-iss-irpf;
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase >= 1903.99 && vbase <= 2826.65){
            var aliquota = 0.075;
            var parc_deduzir = 142.80;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq = vbruto-inss-iss-irpf;
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase >= 2826.66 && vbase <= 3751.05){
            var aliquota = 0.15;
            var parc_deduzir = 354.80;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq = vbruto-inss-iss-irpf;
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase >= 3751.06 && vbase <= 4664.68){
            var aliquota = 0.225;
            var parc_deduzir = 636.13;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq = vbruto-inss-iss-irpf;
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase > 4664.68){
            var aliquota = 0.275;
            var parc_deduzir = 869.36;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq = vbruto-inss-iss-irpf;
            $('#id_valor_liquido').val(vliq);
            }
    });
});
*/