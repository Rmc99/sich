$(document).ready(function () {
    var $id_ano = $("#id_ano");
    $id_ano.mask('0000', {reverse: true});

    //Deixa somente leitura e na cor cinza os campos
    $('#id_valor_bruto').prop('readonly', true);
    $("#id_valor_bruto").css('background', '#DCDCDC');
    $('#id_valor_inss').prop('readonly', true);
    $("#id_valor_inss").css('background', '#DCDCDC');
    $('#id_valor_iss').prop('readonly', true);
    $("#id_valor_iss").css('background', '#DCDCDC');
    $('#id_deducao_irpf').prop('readonly', true);
    $("#id_deducao_irpf").css('background', '#DCDCDC');
    $('#id_valor_pos_deducao_irpf').prop('readonly', true);
    $("#id_valor_pos_deducao_irpf").css('background', '#DCDCDC');
    $('#id_valor_irpf').prop('readonly', true);
    $("#id_valor_irpf").css('background', '#DCDCDC');
    $('#id_valor_liquido').prop('readonly', true);
    $("#id_valor_liquido").css('background', '#DCDCDC');
    $('#id_valor_patronal').prop('readonly', true);
    $("#id_valor_patronal").css('background', '#DCDCDC');
});