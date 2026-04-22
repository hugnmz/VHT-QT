from app.plugins.plugin_base import InstrumentPlugin, check_connection
from enum import Enum


class FrequencyMode(Enum):
    CW = "CW"
    FIXed = "FIXed"

class TriggerMode(Enum):
    FRUN = "FRUN"
    TRIGGERED = "TRIGGERED"
    GATED = "GATED"

class SeparatorMode(Enum):
    TAB = "TAB"
    SEM = "SEMicolon"
    COMM = "COMMa"
    SPACE = "SPACE"
    DOT = "DOT"

class OptimizationMode(Enum):
    EVM = "EVM"
    ACP = "ACP"


class AgilentMXGN5182B(InstrumentPlugin):
    """
    Plugin cho dòng máy Agilent MXG Vector Signal Generator N5182B.
    """

    class Protocol(Enum):
        GPIB = "GPIB"

    def __init__(self):
        super().__init__()
        self.id = "21754dc6-d54f-4d63-b663-7847e55c387e"
        self.name = "Agilent MXG Vector Signal Generator N5182B"
        self.vendor = "Agilent"
        self.description = "MXG Vector Signal Generator"

        self.method_params.update({
            "set_Frequency": [
                {
                    "label": "Frequency Mode",
                    "description": "Mode of frequency setting",
                    "input_type": "enum",
                    "enum_class": FrequencyMode
                },
                {
                    "label": "Frequency",
                    "description": "Frequency value",
                    "input_type": "float_with_unit",
                    "supported_units": ["Hz", "kHz", "MHz", "GHz"]
                }
            ],
            "set_Output_Amplitude": [
                {
                    "label": "Amplitude",
                    "description": "Output power level",
                    "input_type": "float_with_unit",
                    "supported_units": ["dBm", "dBuV", "V"]
                }
            ],
            "set_ARB_SampleClock": [
                {
                    "label": "Sample Clock",
                    "description": "ARB sample clock rate",
                    "input_type": "float_with_unit",
                    "supported_units": ["Hz", "kHz", "MHz"]
                }
            ],
            "set_ARB_RScaling": [
                {
                    "label": "RScaling",
                    "description": "Runtime scaling (%)",
                    "input_type": "float"
                }
            ],
            "set_Modulation_Attenuation_Auto": [
                {
                    "label": "Auto",
                    "description": "Enable/disable auto attenuation",
                    "input_type": "bool"
                }
            ],
            "set_Modulation_Attenuation": [
                {
                    "label": "Attenuation",
                    "description": "Modulator attenuation",
                    "input_type": "float_with_unit",
                    "supported_units": ["dB"]
                }
            ],
            "set_Internal_Channel_Correction_State": [
                {
                    "label": "State",
                    "description": "Enable/Disable I/Q correction",
                    "input_type": "bool",
                }
            ],
            "get_Internal_Channel_Correction_State": [], 
            "execution_Cal_BBG_Channel": [],
            "set_Memory_Load_Channel": [
                {
                    "label": "Channel",
                    "description": "Load data from file to memory",
                    "input_type": "string"
                }
            ],
            "set_Memory_Store_Channel": [
                {
                    "label": "Channel",
                    "description": "Store data into file",
                    "input_type": "string"
                }
            ],
            "set_ARB_Header_RMS": [
                {
                    "label": "RMS filename",
                    "description": "Save the RMS value to a file",
                    "input_type": "string"
                },
                {
                    "label": "RMS value",
                    "description" : "Value RMS voltage setting for file",
                    "input_type": "string"
                }
            ],
            "get_ARB_Header_RMS": [
                {
                    "label" : "filename",
                    "description" : "Name file need to query",
                    "input_type": "string" 
                }
            ],
            "set_Internal_Train_Trigger": [
                {
                    "label": "Trigger Mode",
                    "description": "elect the trigger mode for the pulse train",
                    "input_type" : "enum",
                    "supported_units": TriggerMode
                }
            ],
            "execute_Pulse_Train_Trigger_Immediate": [],
            "execution_Train_List_Preset": [],
            "set_Train_Offtime": [
                {
                    "label" : "Offtime",
                    "description" : "Set Off time (20ns to 42s)",
                    "input_type" : "float_with_unit",
                    "supported_units" : ["ns", "us", "ms", "s"]
                }
            ],

            "get_Train_Offtime": [],
            "get_Train_Offtime_Points": [],
            "set_Train_Ontime" : [
                {

                    "label" : "Ontime",
                    "description" : "Set ON time (20ns to 42s)",
                    "input_type" : "float_with_unit",
                    "supported_units" : ["ns", "us", "ms", "s"]
                }
            ],

            "get_Train_Ontime" : [],
            "get_Train_Ontime_Points" : [],
            "set_Train_Repetition" : [
                {
                    "label" : "Repetition",
                    "description" : "Set repeat count (1 to 2047)",
                    "input_type" : "int"
                }
            ],
            "get_Train_Repetition" : [],
            "get_Train_Repetition_Points" : [],
            "get_Memory_Catalog_PTrain": [],
            "set_Memory_Load_PTrain": [
                {
                    "label": "Filename",
                    "description": "Load .ptrain file from memory.",
                    "input_type": "string"
                }
            ],
            "set_Memory_Store_PTrain": [
                {
                    "label": "Filename",
                     "description": "Store current train to .ptrain file.", 
                     "input_type": "string"
                }
            ],
            "set_Export_Separator_Column": [
                {
                    "label": "Separator", 
                    "description": "Set column separator",
                    "input_type": "enum",
                    "supported_units": SeparatorMode
                }
            ],
            "get_Export_Separator_Column": [],
            "set_Export_Separator_Decimal": [
                {
                    "label": "Decimal",
                    "description": "Set export decimal separator",
                    "input_type": "enum",
                    "supported_units": SeparatorMode
                }
            ],
            "get_Export_Separator_Decimal": [],
            "set_Import_PTrain" : [
                {
                    "label" : "Filename",
                    "description" : "Import pulse train from ASCII file.",
                    "input_type": "string"
                }
            ],
            "set_Import_Separator_Decimal": [
                {
                    "label": "Decimal",
                    "description": "Set import decimal separator",
                    "input_type": "enum",
                    "supported_units": SeparatorMode
                }
            ],
            "get_Import_Separator_Decimal": [],
            "set_Memory_Load_PTrain": [
                {
                    "label": "Filename",
                    "description": "Load .ptrain file from memory.",
                    "input_type": "string"
                }
            ],
            "set_Memory_Store_PTrain": [
                {
                    "label": "Filename",
                    "description": "Store current train to .ptrain file.",
                    "input_type": "string"
                }
            ],
            "set_Internal_Channel_Optimization" : [
                {
                    "label" : "Optimization Mode",
                    "description" : "Select between optimizing mode",
                    "input_type" : "enum",.
                    "supported_units" : OptimizationMode
                }
            ],
            "get_Internal_Channel_Optimization": []
        })

    # --- IMPLEMENTATION METHODS ---

    @check_connection()
    def set_Frequency(self, input: dict):
        """
        Thiết lập tần số sóng mang.
        SCPI:
        :SOURce:FREQuency:CW <value><unit>
        :SOURce:FREQuency:FIXed <value><unit>
        """

        freq_data = input.get("Frequency")
        if not freq_data:
            return False, "Thiếu dữ liệu Frequency", {}, None

        value = freq_data.get("value")
        unit = freq_data.get("unit")

        if value is None or unit is None:
            return False, "Thiếu value hoặc unit", {}, None

        unit = unit.upper()

        mode = input.get("Frequency Mode")

        if mode not in ("CW", "FIXed"):
            return False, "Frequency Mode không hợp lệ", {}, None

        cmd = f":SOURce:FREQuency:{mode} {value}{unit}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", { "mode": mode, "frequency": value, "unit": unit }, raw_value

    @check_connection()
    def set_Output_Amplitude(self, input: dict):
        """
        Thiết lập công suất đầu ra (amplitude).
        SCPI:
        :SOURce:POWer:LEVel:IMMediate:AMPLitude <value><unit>
        """

        amp_data = input.get("Amplitude")
        if not amp_data:
            return False, "Thiếu dữ liệu Amplitude", {}, None

        value = amp_data.get("value")
        unit = amp_data.get("unit")

        if value is None or unit is None:
            return False, "Thiếu value hoặc unit", {}, None

        unit = unit.upper()

        # validate unit cơ bản (tùy thiết bị, thường là dBm)
        if unit not in ("DBM", "DBUV", "V"):
            return False, "Unit không hợp lệ", {}, None

        cmd = f":SOURce:POWer:LEVel:IMMediate:AMPLitude {value}{unit}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"amplitude": value, "unit": unit}, raw_value


    @check_connection()
    def set_ARB_SampleClock(self, input: dict):
        """
        Thiết lập tốc độ lấy mẫu ARB.
        SCPI:
        :SOURce:RADio:ARB:SCLock <value><unit>
        """

        data = input.get("Sample Clock")
        if not data:
            return False, "Thiếu dữ liệu Sample Clock", {}, None

        value = data.get("value")
        unit = data.get("unit")

        if value is None or unit is None:
            return False, "Thiếu value hoặc unit", {}, None

        unit = unit.upper()

        if unit not in ("HZ", "KHZ", "MHZ"):
            return False, "Unit không hợp lệ", {}, None

        cmd = f":SOURce:RADio:ARB:SCLock {value}{unit}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {
            "sample_clock": value,
            "unit": unit
        }, raw_value

    @check_connection()
    def set_ARB_RScaling(self, input: dict):
        """
        Thiết lập Runtime Scaling cho ARB.
        SCPI:
        :SOURce:RADio:ARB:RSCaling <value>
        """

        value = input.get("RScaling")

        if value is None:
            return False, "Thiếu giá trị RScaling", {}, None

        try:
            value = float(value)
        except:
            return False, "RScaling phải là số", {}, None

        if not (0 <= value <= 100):
            return False, "RScaling phải trong khoảng 0-100 (%)", {}, None

        cmd = f":SOURce:RADio:ARB:RSCaling {value}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {
            "rscaling": value
        }, raw_value

    @check_connection()
    def set_Modulation_Attenuation_Auto(self, input: dict):
        """
        Bật/tắt chế độ tự động cho Modulation Attenuation.
        SCPI:
        :SOURce:RADio:ARB:IQ:MODulation:ATTen:AUTO ON|OFF
        """

        value = input.get("Auto")

        if value is None:
            return False, "Thiếu giá trị Auto", {}, None

        # normalize input
        if isinstance(value, bool):
            value = "ON" if value else "OFF"
        else:
            return False, "Auto không hợp lệ", {}, None

        cmd = f":SOURce:RADio:ARB:IQ:MODulation:ATTen:AUTO {value}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {
            "auto": value
        }, raw_value

    @check_connection()
    def set_Modulation_Attenuation(self, input: dict):
        """
        Thiết lập suy hao bộ điều chế.
        SCPI:
        :SOURce:RADio:ARB:IQ:MODulation:ATTen <value><unit>
        """

        data = input.get("Attenuation")
        if not data:
            return False, "Thiếu dữ liệu Attenuation", {}, None

        value = data.get("value")
        unit = data.get("unit")

        if value is None or unit is None:
            return False, "Thiếu value hoặc unit", {}, None

        unit = unit.upper()

        if unit != "DB":
            return False, "Unit phải là dB", {}, None

        try:
            value = float(value)
        except:
            return False, "Attenuation phải là số", {}, None

        if not (0 <= value <= 50):
            return False, "Attenuation phải trong khoảng 0-50 dB", {}, None

        cmd = f":SOURce:RADio:ARB:IQ:MODulation:ATTen {value}{unit}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {
            "attenuation": value,
            "unit": unit
        }, raw_value


    #=================================hùng======================================#

    @check_connection()
    def set_Internal_Channel_Correction_State(self, input: dict):
        """
        Bật hoặc tắt việc áp dụng hiệu chỉnh biên độ và pha
        SCPI Commands:
        SCPI: :SOURce:DM:INTernal:CHANnel:CORRection:STATe <value>
        """

        data = input.get("State")

        if data is None:
            return False, "Thiếu dữ liệu State", {}, None

        if isinstance(data, bool):
            value = "ON" if data else "OFF"
        else:
            return False, "Dữ liệu nhập vào không phải kiểu bool", {}, None

        cmd = f":SOURce:DM:INTernal:CHANnel:CORRection:STATe {value}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK",{"State" : value}, raw_value

    @check_connection()
    def get_Internal_Channel_Correction_State(self, input: dict):

        """
        Truy vấn trạng thái Bật/Tắt của hiệu chỉnh biên độ và pha.
        SCPI: 
        :SOURce:DM:INTernal:CHANnel:CORRection:STATe?
        """

        cmd = f":SOURce:DM:INTernal:CHANnel:CORRection:STATe?"
        raw_value = self._send_command(cmd=cmd)

        if raw_value is None:
            return False, "Không nhận được phản hồi từ thiết bị", {}, None

        response = raw_value.strip() in ("1", "ON")
        return True, "OK", {"is_enable": response}, raw_value

    @check_connection()
    def execution_Cal_BBG_Channel(self, input: dict):
        """
        Thực hiện hiệu chuẩn ngay.
        SCPI:
        :CALibration:BBG:CHANnel
        """

        cmd = f":CALibration:BBG:CHANnel"
        raw_value = self._send_command(cmd=cmd)
        return True, "OK", {}, raw_value

    @check_connection()
    def set_Memory_Load_Channel(self, input: dict):

        """
        Load dữ liệu hiệu chuẩn từ file vào bộ nhớ
        SCPI Commands: 
        :MEMory:LOAD:CHANnel <filename>
        """

        filename = input.get("Channel")

        if not filename:
            return False, "Thiếu filename", {}, None

        cmd = f":MEMory:LOAD:CHANnel "{filename}""

        raw_value = self._send_command(cmd=cmd)
        return True, "OK", {"filename": filename}, raw_value

    @check_connection()
    def set_Memory_Store_Channel(self, input: dict):

        """
        Lưu trữ dữ liệu hiệu chuẩn vào file
        SCPI Commands: 
        :MEMory:STORe:CHANnel <"filename">
        """

        filename = input.get("Channel")

        if not filename:
            return False, "Thiếu filename", {}, None

        cmd = f":MEMory:STORe:CHANnel "{filename}""

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"filename": filename}, raw_value

    @check_connection()
    def set_ARB_Header_RMS(self, input: dict):
        """
        Thiết lập giá trị điện áp RMS cho header của file
        SCPI Commands:
        :SOURce:RADio:ARB:HEADER:RMS <"file_name">,<val>
        """

        filename = input.get("RMS Filename")

        value = input.get("RMS value")

        if not filename:
            return False, "Thiếu filename", {}, None

        if value is None:
            return False, "Thiếu value", {}, None

        if isinstance(value, float):
            try:
                value = float(value)
            except:
                return False, "Value phải là định dạng số hoặc unspecified", {}, None

        elif isinstance(value, str):
            value = value.strip.lower()
            if value != "unspecified":
                return False, "Value phải là định dạng số hoặc unspecified", {}, None         

        cmd = f":SOURce:RADio:ARB:HEADER:RMS "{filename}",{value}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"filename" : filename, "value" : value}, raw_value

    @check_connection()
    def get_ARB_Header_RMS(self, input: dict):
        """

        Truy vấn giá trị điện áp RMS từ header của file
        SCPI Commands:
        :SOURce:RADio:ARB:HEADER:RMS? <"file_name">
        """

        filename = input.get("filename")

        if not filename:
            return False, "Thiếu filename", {}, None

        cmd = f":SOURce:RADio:ARB:HEADER:RMS? "{filename}""

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"filename" : filename}, raw_value

    @check_connection()
    def set_Internal_Train_Trigger(self, input: dict):
        """
        Chọn chế độ kích hoạt cho chuỗi xung.
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:TRIGger <mode>
        """
    
        mode = input.get("Trigger Mode")

        if not mode:
            return False, "Thiếu thông tin về trigger mode", {}, None

        if mode not in TriggerMode
            return False, f"Mode '{mode}' không hợp lệ", {}, None

        cmd = f":SOURce:PULM:INTernal:TRAin:TRIGger {mode}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Trigger Mode" : mode}, raw_value


    @check_connection()
    def execute_Pulse_Train_Trigger_Immediate(self, input: dict):
        """
        Thực hiện chạy chuỗi xung
        SCPI Commands:
         :PULM:INTernal:TRAin:TRIGger:IMMediate
        """


        cmd = ":PULM:INTernal:TRAin:TRIGger:IMMediate"

        raw_value = self._send_command(cmd=cmd)

        return True,"OK", {}, raw_value

    @check_connection()
    def execution_Train_List_Preset(self, input: dict):
        """
        Thực hiện reset bảng Pulse train
        SPCI Commands:
        :SOURce:PULM:INTernal:TRAin:LIST:PRESet
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:LIST:PRESet"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {}, raw_value

    @check_connection()
    def set_Train_Offtime(self, input: dict):

        """
        Thiết lập thời gian ON
        SCPI Commands: 
        :SOURce:PULM:INTernal:TRAin:OFFTime <value><unit>
        """

        data = input.get("Offtime")

        if data is None:
            return False, "Thiếu dữ liệu Offtime", {}, None

        value = data.get("value")
        unit = data.get("unit")

        if value is None:
            return False, "Thiếu dữ liệu value", {}, None

        if value < 20 or value > 42:
            return False, "Value phải nằm trong khoảng 20 - 42", {}, None

        if not unit:
            return False, "Thiếu dữ liệu unit", {}, None

        unit = unit.upper();

        if unit not in ("NS", "US", "MS", "S"):
            return False, "Unit không hợp lệ",{}, None

        cmd = f":SOURce:PULM:INTernal:TRAin:OFFTime {value}{unit}"

        return True, "OK", {"Offtime" : value, "unit" : unit}, raw_value

    @check_connection()
    def get_Train_Offtime(self, input: dict):
        """
        Truy vấn thời gian OFF của điểm chuỗi xung hiện tại
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:OFFTime?
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:OFFTime?"


        raw_value = self._send_command(cmd=cmd)
        if raw_value is None:
            return False, "Không nhận được phản hồi danh sách OFFTime", {}, None
        try:
            value = raw_value.strip()
        except:
            value = raw_value

        return True, "OK", {"Offtime" : value}, raw_value

    @check_connection()
    def get_Train_Offtime_Point(self, input: dict):
        """
        Truy vấn toàn bộ danh sách các điểm OFF Time trong chuỗi xung

        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:OFFTime:POINts?
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:OFFTime:POINts?"

        raw_value = self._send_command(cmd=cmd)
        if raw_value is None:
            return False, "Không nhận được phản hồi danh sách OFFTime", {}, None

        try:
            points = [p.strip() for p in raw_value.split(',')]
        except:
            return False, f"Lỗi bóc tách dữ liệu", {}, raw_value

        return True, "OK", {
            "points": points,
            "count": len(points)
        }, raw_value

    @check_connection()
    def set_Train_Ontime(self, input: dict):
        """
        Thiết lập thời gian ON cho điểm hiện tại
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:ONTime <value><unit>
        """

        data = input.get("Ontime")

        if data is None:
            return False, "Thiếu dữ liệu On time", {}, None

        value = data.get("value")
        unit = data.get("unit")

        if value is None:
            return False, "Thiếu giá trị value", {},None

        if value < 20 or value >42:
            return False, "Giá trị value phải nằm trong khoảng 20 - 42", {},None

        unit = unit.upper()

        if unit not in ("NS", "US", "MS", "S"):
            return False, "Unit không hợp lệ",{}, None

        cmd = f":SOURce:PULM:INTernal:TRAin:ONTime {value}{unit}"

        raw_value = cmd._send_command(cmd=cmd)

        return True, "OK", {"Ontime" : value, "unit": unit}, raw_value

    @check_connection()
    def get_Train_Ontime(self, input: dict):
        """
        Truy vấn ON Time của điểm hiện tại
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:ONTime?
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:ONTime?"

        raw_value = self._send_command(cmd=cmd)
        if not raw_value: 
            return False, "Thiết bị không phản hồi", {}, None

        return True, "OK", {"Ontime": raw_value.strip() if raw_value else None}, raw_value


    @check_connection()
    def get_Train_Ontime_Points(self, input: dict):
        """
        Truy vấn toàn bộ mảng ON Time trong bảng
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:ONTime:POINts?
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:ONTime:POINts?"

        raw_value = self._send_command(cmd=cmd)

        if not raw_value:
            return False, "Thiết bị không phản hồi danh sách", {}, None

        points = [p.strip() for in raw_value.split(',')]

        return True, "OK", {"points": points, "count": len(points)}, raw_value


    @check_connection()
    def set_Train_Repetition(self, input: dict):
        """
        Thiết lập số lần lặp lại cho điểm hiện tại
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:REPetition {value}
        """

        value = input.get("Repetition")

        if not value:
            return False, "Thiếu dữ liệu value", {}, None

        try:
            value = int(value)
        except:
            return False, "value phải là số nguyên", {}, None

        if value <= 0 or value >= 2048 :
            return False, "value phải nằm trong khoảng 1 - 2047", {}, None

        cmd = f":SOURce:PULM:INTernal:TRAin:REPetition {value}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Repetition" : value}, raw_value

    @check_connection()
    def get_Train_Repetition(self, input: dict):
        """
        Truy vấn số lần lặp lại của điểm hiện tại
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:REPetition?
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:REPetition?"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Repetition": raw_value.strip() if raw_value else None}, raw_value


    @check_connection()
    def get_Train_Repetition_Points(self, input: dict):

        """
        Truy vấn toàn bộ mảng số lần lặp lại.
        SCPI Commands:
        :SOURce:PULM:INTernal:TRAin:REPetition:POINts?
        """

        cmd = ":SOURce:PULM:INTernal:TRAin:REPetition:POINts?"

        raw_value = self._send_command(cmd=cmd)

        if not raw_value:
            return False, "Thiết bị không phản hồi danh sách", {}, None

        points = [p.strip() for p in raw_value.split(',')]

        return True, "OK", {"points": points, "count": len(points)}, raw_value

    @check_connection()
    def get_Memory_Catalog_PTrain(self, input: dict):
        """
        Truy vấn danh sách các file .ptrain trong bộ nhớ.
        SCPI Commands
        :MEMory:CATalog:PTRain?
        """

        raw_value = self._send_command(":MEMory:CATalog:PTRain?")
        return True, "OK", {"catalog": raw_value}, raw_value


    @check_connection()
    def set_Memory_Load_PTrain(self, input: dict):
        """
        Tải file .ptrain vào máy
        SCPI Commands:
        :MEMory:EXPort:ASCii:PTRain <"filename">
        """

        filename = input.get("Filename")

        if not filename:
            return False, "Thiếu filename đầu vào", {}, None

        cmd = f":MEMory:EXPort:ASCii:PTRain "{filename}""

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"filename" : filename}, raw_value

    @check_connection()
    def set_Export_Separator_Column(self, input: dict):

        """
        Thiết lập dấu phân cách cột
        SCPI Commands:
        :MEMory:EXPort:ASCii:SEParator:COLumn <mode>
        """

        mode = input.get("Separator")

        if not mode:
            return False, "Thiếu dữ liệu mode", {}, None

        if mode not in ("TAB", "SEMicolon", "COMMa", "SPACE")
            return False, "Dữ liệu mode không hợp lệ", {}, None

        cmd = f":MEMory:EXPort:ASCii:SEParator:COLumn {mode}"

        return True, "OK", {"Separator": mode}, self._send_command(cmd)

    @check_connection()
    def get_Export_Separator_Column(self, input: dict):
        """ 
        Truy vấn dấu phân cách cột hiện tại
        SCPI Commands:
        :MEMory:EXPort:SEParator:COLumn?
        """

        raw_value = self._send_command(":MEMory:EXPort:SEParator:COLumn?")

        if not raw_value:
            return False, "Hệ thống không phản hổi", {}, None

        return True, "OK", {"Separator Column": raw_value.strip()}, None

    
    @check_connection()
    def set_Export_Separator_Decimal(self, input: dict):
        """
            Thiết lập dấu thập phân khi EXPORT
            SCPI Commands:
            :MEMory:EXPort:ASCii:SEParator:DECimal <mode>
        """

        mode = data.get("Decimal")

        if not mode:
            return False, "Thiếu dữ liệu mode", {}, None

        if mode not in ("DOT", "COMMa")
            return False, "Dữ liệu mode không hợp lệ", {}, None

        cmd = f":MEMory:EXPort:ASCii:SEParator:DECimal {mode}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Export Decimal": mode}, raw_value

    
    @check_connection()
    def get_Export_Separator_Decimal(self, input: dict):
        """
        Truy vấn dấu thập phân khi EXPORT
        SCPI Commands:
        :MEMory:EXPort:ASCii:SEParator:DECimal?
        """

        raw_value = self._send_command(":MEMory:EXPort:ASCii:SEParator:DECimal")

        if not raw_value:
            return False, "Hệ thống không phản hồi", {}, None

        return True, "OK", {"Export Decimal" : raw_value.strip()}, raw_value

    @check_connection()
    def set_Import_PTrain(self, input: dict):
        """
        Nhập dữ liệu chuỗi xung từ file văn bản
        SCPI Commands:
        :MEMory:IMPort:ASCii:PTRain <"filename">
        """

        filename = input.get("Filename")

        if not filename:
            return False, "Thiếu dữ liệu filename", {}, None

        cmd = f":MEMory:IMPort:ASCii:PTRain "{filename}""

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Filename" : filename}, raw_value

    @check_connection()
    def set_Import_Separator_Decimal(self, input: dict):

        """
        Thiết lập dấu thập phân khi IMPORT
        SCPI Commands:
        :MEMory:IMPort:ASCii:SEParator:DECimal <mode>
        """

        mode = input.get("Decimal")

        if not mode:
            return False, "Thiếu dữ liệu mode", {}, None

        if mode not in ("DOT", "COMMa"):
            return False, "Dữ liệu mode không hợp lệ", {}, None

        cmd = f":MEMory:IMPort:ASCii:SEParator:DECimal {mode}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Import Decimal" : mode}, raw_value

    @check_connection()
    def get_Import_Separator_Decimal(self, input: dict):
        """
        Truy vấn dấu thập phân khi IMPORT.
        SCPI Commands:
        :MEMory:IMPort:ASCii:SEParator:DECimal?
        """

        cmd = ":MEMory:IMPort:ASCii:SEParator:DECimal?"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Import Decimal": raw_value.strip() if raw_value else None}, raw_value


    @check_connection()
    def set_Memory_Load_PTrain(self, input: dict):

        """
        Tải file .ptrain vào máy
        SCPI Commands:
        :MMEMory:LOAD:PTRain <"filename">
        """


        filename = input.get("Filename")

        if not filename:
            return False, "Thiếu dữ liệu filename", {}, None

        cmd = f":MMEMory:LOAD:PTRain "{filename}""

        raw_value = self._send_command(cmd=cmd)
        return True, "OK", {"Filename" : filename}, raw_value

    @check_connection()
    def set_Memory_Store_PTrain(self, input: dict):
        """
        Lưu chuỗi xung hiện tại thành file .ptrain
        SCPI Commands:
        :MMEMory:STORe:PTRain <"filename">
        """

        filename = input.get("Filename")

        if not filename:
            return False, "Thiếu dữ liệu filename", {}, None

        cmd = f":MMEMory:STORe:PTRain "{filename}""

        raw_value = self._send_command(cmd=cmd)
        return True, "OK", {"Filename" : filename}, raw_value


    @check_connection()
    def set_Internal_Channel_Optimization(self, input: dict):

        """
            Tối ưu hóa kênh I/Q nội bộ cho EVM hoặc ACP
            SCPI Commands:
            :SOURce:DM:INTernal:CHANnel:OPTimization <mode>
        """

        mode = input.get("Optimization Mode")
        if mode not in ["EVM", "ACP"]:
            return False, "Mode không hợp lệ (EVM hoặc ACP)", {}, None

        cmd = f":SOURce:DM:INTernal:CHANnel:OPTimization {mode}"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Optimization": mode}, raw_value

    @check_connection()
    def get_Internal_Channel_Optimization(self, input: dict):

        """
        Truy vấn chế độ tối ưu hóa I/Q hiện tại
        SCPI Commands: 
        :SOURce:DM:INTernal:CHANnel:OPTimization?
        """

        cmd = ":SOURce:DM:INTernal:CHANnel:OPTimization?"

        raw_value = self._send_command(cmd=cmd)

        return True, "OK", {"Optimization": raw_value.strip() if raw_value else None}, raw_value
        