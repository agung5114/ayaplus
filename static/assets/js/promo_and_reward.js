const notif_promo = document.getElementById('notif_promo');
setTimeout(() => {
  notif_promo.classList.remove ('d-none');
}, 2000); 

const notif_reward = document.getElementById('notif_reward');
setTimeout(() => {
  notif_reward.classList.remove ('d-none');
}, 4000); 


// show_hide_nama_peserta_terutang_dan_nomor_kartu_terutang('id_nomor_kartu_terutang', id_nama_peserta_terutang , 'diri_sendiri')"
function show_hide_inputan_nama_peserta_terutang_dan_nomor_kartu_terutang(targetId1,targetId2, triggerValue) {
  const value_tipe_pembayaran = document.querySelector('option:checked').value;
  if (value_tipe_pembayaran == triggerValue) {
    document.getElementById(targetId1).classList.remove("d-none");
    document.getElementById(targetId2).classList.remove("d-none");
  } else {
    document.getElementById(targetId1).classList.add("d-none");
    document.getElementById(targetId2).classList.add("d-none");
  }
}

function show_hide_nama_peserta_terutang(){
  const nomor_kartu_terutang = document.querySelector('input[id="nomor_kartu_terutang"]').value;
  if(nomor_kartu_terutang == '0002741016577'){
    nama_peserta_terutang.setAttribute("value","Fadia Sabrina Ganafi");
  } else {
    nama_peserta_terutang.setAttribute("value","Khaizuran Al-Kayyis");
  }
}



function showHideEle(targetEleId, triggerValue) {
  const value_jenis_kepesertaan = document.querySelector('input[name="tipe_kepesertaan"]:checked').value;
  if (value_jenis_kepesertaan == triggerValue) {
    document.getElementById(targetEleId).classList.remove("d-none");
  } else {
    document.getElementById(targetEleId).classList.add("d-none");
  }
}

function hitungJumlahBayar() {
  const value_jenis_kepesertaan = document.querySelector('input[name="tipe_kepesertaan"]:checked').value;
  const value_tipe_kelas = document.querySelector('input[name="tipe_kelas"]:checked').value;
  const id_jumlah_bayar_per_bulan = document.getElementById("jumlah_bayar_per_bulan");
  const id_jumlah_bayar_per_bundle = document.getElementById("jumlah_bayar_per_bundle");
  const id_jumlah_penghematan = document.getElementById("jumlah_penghematan");
  const jumlah_checkbox_yang_dicentang = document.querySelectorAll('input[type="checkbox"]:checked').length;
  const jumlah_bayar_per_bulan = 35000;
  const biaya_per_bulan_kelas_1 = 150000;
  const biaya_per_bulan_kelas_2 = 100000;

  if (value_jenis_kepesertaan == "PBI" || (value_jenis_kepesertaan =="PBPU" && value_tipe_kelas =="kelas_3")) {
    if(jumlah_checkbox_yang_dicentang == 1){
      id_jumlah_bayar_per_bulan.setAttribute("value","Rp. " + jumlah_bayar_per_bulan);
      id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + 0);
      id_jumlah_penghematan.setAttribute("value","Rp. " + 0);
    } else if (jumlah_checkbox_yang_dicentang > 1 && jumlah_checkbox_yang_dicentang <= 3){
      const jumlah_bayar = jumlah_checkbox_yang_dicentang * jumlah_bayar_per_bulan * 0.9;
      const jumlah_penghematan = jumlah_checkbox_yang_dicentang * jumlah_bayar_per_bulan * 0.1;
      id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + jumlah_bayar);
      id_jumlah_penghematan.setAttribute("value","Rp. " + jumlah_penghematan);

    } else {
      const jumlah_bayar = jumlah_checkbox_yang_dicentang * jumlah_bayar_per_bulan * 0.7;
      const jumlah_penghematan = jumlah_checkbox_yang_dicentang * jumlah_bayar_per_bulan * 0.3;
      id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + jumlah_bayar);
      id_jumlah_penghematan.setAttribute("value","Rp. " + jumlah_penghematan);
    }




  } else {
    // Jenis kepestaan PBPU selain kelas 3 (karena kelas 3 tarifnya sama kayak PBI)
    if (value_tipe_kelas == "kelas_2"){
      // PBU Kelas 2
      if(jumlah_checkbox_yang_dicentang == 1){
        id_jumlah_bayar_per_bulan.setAttribute("value","Rp. " + biaya_per_bulan_kelas_2);
        id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + 0);
        id_jumlah_penghematan.setAttribute("value","Rp. " + 0);
      } else if (jumlah_checkbox_yang_dicentang > 1 && jumlah_checkbox_yang_dicentang <= 3){
        const jumlah_bayar = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_2 * 0.9;
        const jumlah_penghematan = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_2 * 0.1;
        id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + jumlah_bayar);
        id_jumlah_penghematan.setAttribute("value","Rp. " + jumlah_penghematan);
      }
      else {
        const jumlah_bayar = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_2 * 0.7;
        const jumlah_penghematan = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_2 * 0.3;
        id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + jumlah_bayar);
        id_jumlah_penghematan.setAttribute("value","Rp. " + jumlah_penghematan);
      }

      
    }else{
      // Kelas 1 
      if(jumlah_checkbox_yang_dicentang == 1){
        id_jumlah_bayar_per_bulan.setAttribute("value","Rp. " + biaya_per_bulan_kelas_1);
        id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + 0);
        id_jumlah_penghematan.setAttribute("value","Rp. " + 0);
      } else if (jumlah_checkbox_yang_dicentang > 1 && jumlah_checkbox_yang_dicentang <= 3){
        const jumlah_bayar = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_1 * 0.9;
        const jumlah_penghematan = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_1 * 0.1;
        id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + jumlah_bayar);
        id_jumlah_penghematan.setAttribute("value","Rp. " + jumlah_penghematan);
      }
      else {
        const jumlah_bayar = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_1 * 0.7;
        const jumlah_penghematan = jumlah_checkbox_yang_dicentang * biaya_per_bulan_kelas_1 * 0.3;
        id_jumlah_bayar_per_bundle.setAttribute("value","Rp. " + jumlah_bayar);
        id_jumlah_penghematan.setAttribute("value","Rp. " + jumlah_penghematan);
      }
    }


   

    


  }
}
